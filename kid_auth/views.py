from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

from .forms import LoginForm, RegisterNewInstitutionAndUserForm, RegisterNewParentForm
from .models import User, DIRECTOR, ParentInvitation
from main.models import Institution, Address, Children
from kid_info import utility


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'kid_auth/login_view.html', {'form': form})

    def post(self, request, **kwargs):
        form = LoginForm(request.POST)
        error = ''
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
            else:
                error = 'Email lub hasło niepoprawne. '
        return render(
            request,
            'kid_auth/login_view.html',
            {'form': form, 'text': error},
        )


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterInstitution(View):
    """
    Register new Institution and assign with Address and User(also create)
    """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard-home')
        form = RegisterNewInstitutionAndUserForm()
        return render(request, 'kid_auth/institution_register_view.html', {
            'form': form,
        })

    def post(self, request):
        form = RegisterNewInstitutionAndUserForm(request.POST)
        if form.is_valid():
            user_address = Address.objects.create(
                street=form.cleaned_data['user_street'],
                zip_code=form.cleaned_data['user_zip'],
                town=form.cleaned_data['user_town']
            )
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=user_address,
                user_type=DIRECTOR,
            )
            institution_address = Address.objects.create(
                street=form.cleaned_data['institution_street'],
                zip_code=form.cleaned_data['institution_zip'],
                town=form.cleaned_data['institution_town']
            )
            institution = Institution.objects.create(
                name=form.cleaned_data['institution_name'],
                owner=user,
                address=institution_address,
            )
            return redirect('/')
        else:
            return render(request, 'kid_auth/institution_register_view.html', {
                'form': form,
            })


class ParentInvitationView(View):
    def post(self, request):
        rq_id = request.POST.get('id')
        email = request.POST.get('email')
        parent_type = request.POST.get('parent_type')
        my_hash = utility.hash_generator()

        inv = ParentInvitation.objects.create(
            hash=my_hash,
            email=email
        )
        children = Children.objects.get(pk=rq_id)

        if parent_type == '0':
            children.mother_inv = inv
        else:
            children.father_inv = inv

        children.save()

        send_status = utility.send_parent_invitation(email, my_hash)
        if not send_status:
            JsonResponse({
                'error': send_status,
            })

        return JsonResponse({
            'id': inv.id,
            'email': email,
            'send_status': send_status,
        })


class ParentRegistrationViaInv(View):
    def get(self, request, my_hash):
        inv = get_object_or_404(ParentInvitation, hash=my_hash)

        form = RegisterNewParentForm(initial={
            'email': inv.email
        })

        return render(request, 'kid_auth/parent_register_view.html', {
            'inv': inv,
            'form': form,
        })

    def post(self, request, my_hash):
        inv = get_object_or_404(ParentInvitation, hash=my_hash)
        form = RegisterNewParentForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            user_address = Address.objects.create(
                street=form.cleaned_data['user_street'],
                zip_code=form.cleaned_data['user_zip'],
                town=form.cleaned_data['user_town']
            )
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                user_type=1,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=user_address
            )
            if getattr(inv, 'mother_inv', None):
                inv.mother_inv.mother = user
                inv.mother_inv.save()
            else:
                inv.father_inv.father = user
                inv.father_inv.save()

            inv.delete()

        return redirect('login-page')


class ParentInvitationCancelView(View):
    def post(self, request):
        inv_id = request.POST.get('id')

        if inv_id is None or inv_id == '':
            response = JsonResponse({"error": "No id specified"})
            response.status_code = 403
            return response
        else:
            inv = ParentInvitation.objects.get(pk=inv_id)
            inv.delete()

        return JsonResponse({
            'status': 'ok'
        })

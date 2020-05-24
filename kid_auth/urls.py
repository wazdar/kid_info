from django.urls import path
from kid_auth import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login-page'),
    path('logout', views.LogoutView.as_view(), name='logout-page'),
    path('register', views.RegisterInstitution.as_view(), name='register-institution'),
    path('invite', views.ParentInvitationView.as_view(), name='parent-invite'),
    path('invite/cancel', views.ParentInvitationCancelView.as_view(), name='parent-invite-cancel'),
    path('parent/inv/<str:my_hash>', views.ParentRegistrationViaInv.as_view(), name='parent-registration'),
    path('forgotpass/', views.PasswordResetEmailView.as_view(), name='forgot-password'),
    path('password-reset/<str:pass_hash>', views.PasswordResetView.as_view(), name='password-reset'),
]

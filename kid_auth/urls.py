from django.urls import path

from kid_auth import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login-page'),
    path('logout', views.LogoutView.as_view(), name='logout-page')
]

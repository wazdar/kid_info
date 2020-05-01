from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home-page'),
    path('login/', views.UserLoginView.as_view(), name='login-page')
]

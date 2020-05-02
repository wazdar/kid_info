from django.contrib import admin
from django.urls import path, include

from main import views
from kid_auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home-page'),
    path('2', views.HomePageView2.as_view(), name='home-page'),
    path('account/', include(auth_urls))
]

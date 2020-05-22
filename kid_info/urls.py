from django.contrib import admin
from django.urls import path, include

from main import views
from kid_auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home-page'),
    path('2', views.HomePageView2.as_view(), name='home-page'),
    path('account/', include(auth_urls)),

    path('dashboard/', views.DashboardHomeView.as_view(), name='dashboard-home'),
    path('dashboard/kids/', views.DashboardKidsView.as_view(), name='dashboard-kids'),
    path('dashboard/kids/add', views.KidsAddView.as_view(), name='kids-add'),
    path('dashboard/kids/presence', views.KidsPresencesView.as_view(), name='kids-presence'),
    path('dashboard/kids/presence/set', views.KidsPresencesSetView.as_view(), name='kids-presence-set'),
    path('dashboard/kids/presence/get', views.KidsPresencesGetView.as_view(), name='kids-presence-get'),
    path('dashboard/kids/presence/get-all', views.KidsAllPresencesGetView.as_view(), name='kids-presence-get-all'),
    path('dashboard/bills', views.MainBillsView.as_view(), name='bills-home'),


]

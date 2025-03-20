from django.urls import path
from . import views



urlpatterns = [
    path('', views.intro, name='vimo'),

    path('home./', views.home, name='home'),
    path('register,',views.register_user,name='register_user'),
    path('login./',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),

    path('about./',views.about,name='about'),

    path('contact./',views.contact,name='contact'),

    path('dashboard./',views.dashboard,name='dashboard'),




]


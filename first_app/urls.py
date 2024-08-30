from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup , name='signup'),
    path('login/', views.user_login , name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('password_change/',views.pass_change, name='password_change'),
    path('password_reset/',views.pass_reset, name='password_reset'),
]  
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,profile

# from .views import 

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view, name='login'),# .as_view =>  parametreler eklenebilir
    path('register/',register, name='register'),
    path('profile/',profile, name='profile'),
    # path('login/',auth_views.LoginView.as_view(), name='login'),
   
]

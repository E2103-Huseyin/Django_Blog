from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

# from .views import 

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view, name='login'),# .as_view =>  parametreler eklenebilir
    path('register/',register, name='register'),
   
]

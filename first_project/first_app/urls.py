from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
]

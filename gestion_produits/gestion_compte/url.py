from django.urls import path
from gestion_compte.views import singup,logout_user,login_user

urlpatterns = [
    path('singup/',singup,name='singup'),
    path('logout/',logout_user,name='logout'),
    path('login/',login_user,name='login')

    
]
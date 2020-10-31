from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),

    path('auth/registration/', include('dj_rest_auth.registration.urls')),


    
]


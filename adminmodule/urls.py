from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',generalhomepage,name = 'generalhomepage'),
    path('projecthomepage',projecthomepage,name = 'projecthomepage'),
    path('facultyhomepage/',facultyhompage, name = 'facultyhomepage'),
    path('studenthomepage/',studenthomepage,name = 'studenthomepage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signup1/', signup1, name='signup1'),
    path('login1/', login1, name='login1'),
    path('logout/', logout, name='logout'),
]

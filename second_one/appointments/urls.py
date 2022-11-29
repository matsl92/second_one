from django.urls import path
from . import views

app_name = 'appointments'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('personal_info/', views.personal_info, name = 'personal_info'), 
    path('create_gaps/', views.create_gaps, name='create_gaps'),
    path('gaps/', views.gaps, name='gaps'),
    path('gaps/success/', views.success, name='succes'),
]

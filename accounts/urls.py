from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('profile/', TestView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('change/profile/', ChangeProfileView.as_view(), name="change_profile"),
    path('create/', views.minhacompeticao, name='create_competitions'),
    path('homepage/', views.mostrar_competicoes, name='homepage'),
    path('mostrar/', views.mostrar_competicoes, name='mostrarcompeticoes'),
    path('cmodalidade/', views.minhamodalidade, name='create_modality'),
    path('mmodalidade/<int:modalidade_id>', views.mostrar_modalidades, name='mostrarmodalidade'),
    path('cequipes/', views.criar_equipes, name='create_teams'),
    path('mequipes/<int:equipe_id>', views.mostrar_equipes, name='mostrarequipes'),
] 

from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from .forms import *
from django.core.paginator import Paginator

class ProfileView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            kwargs['first_name'] = self.request.user.first_name

        kwargs["title"] = "Profile"

        return super().get_context_data(**kwargs)

class TestView(LoginRequiredMixin, View):
    template_name="profile.html"

    def dispatch(self, request, *args, **kwargs):
        print(request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreation_Form
    success_url = '/accounts/login/'

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

def change_profile(request):
    template_name = "registration/change_profile.html"

    if request.method == "POST":
        form = UserChange_Form(request.POST, instance=request.user)

        password_post = {
            "old_password": request.POST.get("old_password"),
            "new_password1": request.POST.get("new_password1"),
            "new_password2": request.POST.get("new_password2")
        }

        password_change_form = PasswordChange_Form(user=request.user, data=password_post)

        if all([form.is_valid(), password_change_form.is_valid()]):
            form.save()

            return redirect('profile')
    
    else:
        form = UserChange_Form(instance=request.user)
        password_change_form = PasswordChange_Form(user=request.user)
    
    context = {
        "form": form,
        "password_change_form": password_change_form
    }

    return render(request, template_name, context)

class ChangeProfileView(UpdateView):
    template_name = "registration/change_profile.html"
    form_class = UserChange_Form
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        context = self.get_context_data()

        try:
            password_change_form = context['password_change_form']
            if password_change_form.is_valid() and form.is_valid():
                form.save()

                is_authenticated = password_change_form.user.is_authenticated

                password_change_form.save()

                """ 
                    Fazendo login do usuario novamente caso esteja mudando do seu perfil
                """
                update_session_auth_hash(self.request, password_change_form.user)

                return redirect(self.get_success_url())
            
        except KeyError:
            if form.is_valid():
                form.save()
                return redirect(self.get_success_url())
            
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        if self.request.POST:
            context["form"] = self.form_class(self.request.POST, instance=self.request.user)

            password_post = {
                                "old_password": self.request.POST.get("old_password"),
                                "new_password1": self.request.POST.get("new_password1"),
                                "new_password2": self.request.POST.get("new_password2")
                            }
            print(self.request.POST)
            if password_post["old_password"]:
                print("Password")
                context["password_change_form"] = PasswordChange_Form(user=self.request.user, data=password_post)
        
        else:
            context["password_change_form"] = PasswordChange_Form(user=self.request.user)
        
        return context

def minhacompeticao(request):
    template_name = "competition/create_competitions.html"
    if request.method == 'POST':
        form = CompeticaoForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('mostrarcompeticoes')
    else:
        form = CompeticaoForm()
        
    return render(request, template_name, {"form": form})

def mostrar_competicoes(request):
    if request.user.is_superuser:
        competicoes = Competicao.objects.all()
        paginator = Paginator(competicoes,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'competicoes':page_obj}
        return render(request, 'competition/mostrarcompeticoes.html', context)
    else:
        competicoes = Competicao.objects.all()
        paginator = Paginator(competicoes,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'competicoes':page_obj}
        return render(request, 'competition/homepage.html', context)

def minhamodalidade(request):
    template_name = "competition/create_modality.html"

    if request.method == 'POST':
        form = ModalidadeForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('mostrarcompeticoes')
    else:
        form = ModalidadeForm()
        
    return render(request, template_name, {"form": form})

def mostrar_modalidades(request, modalidade_id):
    if request.user.is_superuser:
        modalidades = Modalidade.objects.filter(competicao1__pk = modalidade_id)
        paginator = Paginator(modalidades,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'modalidades': page_obj}
        return render(request, 'competition/mostrarmodalidade.html', context)
    else:
        modalidades = Modalidade.objects.filter(competicao1__pk = modalidade_id)
        paginator = Paginator(modalidades,5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'modalidades': page_obj}
        return render(request, 'competition/mostrarmaluno.html', context)

def criar_equipes(request):
    template_name = "competition/create_teams.html"

    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('mostrarcompeticoes')
    else:
        form = EquipeForm()
    
    return render(request, template_name, {"form":form})

def mostrar_equipes(request, equipe_id):
    if request.user.is_superuser:
        equipes = Equipes.objects.filter(modalidade_equipe__pk = equipe_id)
        #membros = Equipes.objects.filter(participantes__pk = equipe_id)
        context = {'equipes':equipes}
        return render(request, 'competition/mostrarequipes.html',context)
    else:
        equipes = Equipes.objects.filter(modalidade_equipe__pk = equipe_id)
        context = {'equipes':equipes}
        return render(request, 'competition/mostrarequipesaluno.html',context)
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Linguagem, Cadeira, Projeto, Escola, Interesse, Laboratorio, Post, Rede, Quiz
from .forms import PostForm, QuizForm, ProjetoForm

def home_view(request):
	return render(request, 'portfolio/home.html')

def sobre_mim_view(request):
	context = {
        'cadeiras': Cadeira.objects.all(),
        'escolas': Escola.objects.all(),
        'interesses': Interesse.objects.all(),
    }

	return render(request, 'portfolio/sobre_mim.html', context)

def projetos_view(request):
    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:projetos'))

    context = {
        'projetos': Projeto.objects.all(),
        'form': form,
    }

    return render(request, 'portfolio/projetos.html', context)

def criar_projeto_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('portfolio:login'))

    form = ProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:projetos'))

    context = {
        'form': form,
    }

    return render(request, 'portfolio/criar_projeto.html', context)

def pw_view(request):
    form = QuizForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.path_info)

    context = {
        'linguagens': Linguagem.objects.all(),
        'laboratorios': Laboratorio.objects.all(),
        'form': form,
    }

    return render(request, 'portfolio/pw.html', context)

def blog_view(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'portfolio/blog.html', context)

def criar_post_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('portfolio:login'))

    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:blog'))

    context = {
        'form': form,
    }

    return render(request, 'portfolio/criar_post.html', context)

def sobre_website_view(request):
	return render(request, 'portfolio/sobre_website.html')

def contacto_view(request):
    context = {
        'redes': Rede.objects.all(),
    }

    return render(request, 'portfolio/contacto.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {'message': 'Credenciais invalidas.'})

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)

    return render(request, 'portfolio/home.html')

@login_required
def editar_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:blog'))

    context = {
        'form': form, 
        'post_id': post_id
    }

    return render(request, 'portfolio/editar_post.html', context)

@login_required
def apagar_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return HttpResponseRedirect(reverse_lazy('portfolio:blog'))

@login_required
def editar_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:projetos'))

    context = {
        'form': form, 
        'projeto_id': projeto_id
    }

    return render(request, 'portfolio/editar_projeto.html', context)

@login_required
def apagar_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()

    return HttpResponseRedirect(reverse_lazy('portfolio:projetos'))
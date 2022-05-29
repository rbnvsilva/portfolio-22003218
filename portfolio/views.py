from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Linguagem, Cadeira, Projeto, Escola, Interesse, Laboratorio, Post, Rede
from .forms import PostForm, QuizForm

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
	context = {
        'projetos': Projeto.objects.all(),
    }

	return render(request, 'portfolio/projetos.html', context)

def pw_view(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:pw'))

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
            return HttpResponseRedirect(reverse_lazy('portfolio:blog'))
        else:
            return render(request, 'portfolio/login.html', {'message': 'Credenciais invalidas.'})

    return render(request, 'portfolio/login.html')

def logout_view(request):
    logout(request)

    return render(request, 'portfolio/login.html', {'message': 'Terminou sessao'})

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

def apagar_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return HttpResponseRedirect(reverse_lazy('portfolio:blog'))
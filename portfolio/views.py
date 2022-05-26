from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Linguagem, Cadeira, Projeto, Escola, Interesse, Laboratorio, Post
from .forms import PostForm

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
	context = {
        'linguagens': Linguagem.objects.all(),
        'laboratorios' : Laboratorio.objects.all(),
    }

	return render(request, 'portfolio/pw.html', context)

def blog_view(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'portfolio/blog.html', context)

def criar_post_view(request):
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
	return render(request, 'portfolio/contacto.html')
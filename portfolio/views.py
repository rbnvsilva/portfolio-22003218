from django.shortcuts import render
from .models import Pessoa, Linguagem, Cadeira, Projeto, Escola

def home_view(request):
	return render(request, 'portfolio/home.html')

def sobre_mim_view(request):
	context = {
        'cadeiras': Cadeira.objects.all(),
        'escolas': Escola.objects.all(),
    }

	return render(request, 'portfolio/sobre_mim.html', context)

def projetos_view(request):
	return render(request, 'portfolio/projetos.html')

def pw_view(request):
	return render(request, 'portfolio/pw.html')

def blog_view(request):
	return render(request, 'portfolio/blog.html')

def sobre_site_view(request):
	return render(request, 'portfolio/sobre_site.html')

def contacto_view(request):
	return render(request, 'portfolio/contacto.html')
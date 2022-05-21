from django.shortcuts import render

from portfolio.forms import PostForm
from .models import Post
from .forms import PostForm

def home_view(request):
	return render(request, 'portfolio/home.html')

def sobre_mim_view(request):
	return render(request, 'portfolio/sobre_mim.html')

def projetos_view(request):
	return render(request, 'portfolio/projetos.html')

def pw_view(request):
	return render(request, 'portfolio/pw.html')

def blog_view(request):
	form = PostForm(request.POST or None)

	context = {
		'posts': Post.objects.all(),
		'form': form
	}
	
	return render(request, 'portfolio/blog.html', context)

def sobre_site_view(request):
	return render(request, 'portfolio/sobre_site.html')

def contacto_view(request):
	return render(request, 'portfolio/contacto.html')
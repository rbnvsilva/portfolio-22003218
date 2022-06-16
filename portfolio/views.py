from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Linguagem, Cadeira, Projeto, Escola, Interesse, Laboratorio, Post, Rede, Quiz, Noticia
from .forms import PostForm, QuizForm, ProjetoForm, CadeiraForm
from matplotlib import pyplot as plt
import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')

def grafico():
    quizzes = Quiz.objects.all().order_by('pontuacao')
    nomes = [quiz.nome for quiz in quizzes]
    pontuacoes = [quiz.pontuacao for quiz in quizzes]
    
    plt.barh(nomes, pontuacoes)
    plt.xlabel("Pontuacoes")
    plt.ylabel("Nomes")
    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri

def pontuacao(request):
    pontuacao = 0
    if (request.POST['p1'].lower() == "Hypertext Markup Language".lower()):
        pontuacao += 1
    if(request.POST['p2'].lower() == "Python".lower()):
        pontuacao += 1
    if(request.POST['p3'].lower() == "4".lower()):
        pontuacao += 1
    if(request.POST['p4'].lower() == "<b>".lower()):
        pontuacao += 1
    if(request.POST['p5'].lower() == "admin.py".lower()):
        pontuacao += 1
    
    return pontuacao

def home_view(request):
	return render(request, 'portfolio/home.html')

def sobre_mim_view(request):
	context = {
        'cadeiras': Cadeira.objects.all(),
        'escolas': Escola.objects.all(),
        'interesses': Interesse.objects.all(),
    }

	return render(request, 'portfolio/sobre_mim.html', context)

def criar_cadeira_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('portfolio:login'))

    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:sobre_mim'))

    context = {
        'form': form,
    }

    return render(request, 'portfolio/criar_cadeira.html', context)

@login_required
def editar_cadeira_view(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('portfolio:sobre_mim'))

    context = {
        'form': form, 
        'cadeira_id': cadeira_id
    }

    return render(request, 'portfolio/editar_cadeira.html', context)

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

def pw_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao(request)
        r = Quiz(nome=n, pontuacao=p)
        r.save()

    context = {
        'linguagens': Linguagem.objects.all(),
        'laboratorios': Laboratorio.objects.all(),
        'noticias': Noticia.objects.all(),
        'data': grafico()
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
from django import forms
from django.forms import ModelForm
from .models import Post, Quiz, Projeto, Cadeira

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

        labels = {
            'nome_pessoa': 'Nome:',
            'pergunta1': 'Qual o significado da abreviacao HTML?',
            'pergunta2': 'Quais sao os dois tipos que existem no que toca a linguagens para web development?',
            'pergunta3': 'Em qual dos ficheiros da tua app Django podes registar as tuas classes para aparecerem no teu painel de admin?',
            'pergunta4': 'Qual o comando que precisas obrigatoriamente de correr para ter acesso ao painel de admin?',
            'pergunta5': 'O Django foi criado originalmente como sistema para gerenciar publicacoes de emprego (Sim/Nao)?',
        }

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'        
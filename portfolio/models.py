from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    link1 = models.CharField(max_length=300)
    link2 = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nome

class Linguagem(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    tipo = models.IntegerField()
    image = models.FileField(upload_to="uploads/")

    def __str__(self):
        return self.nome

class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=10)
    topicos = models.TextField()
    ranking = models.IntegerField()
    professores = models.ManyToManyField(Pessoa)
    pagina_cadeira = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    ano_realizacao = models.IntegerField()
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE)
    participantes = models.ManyToManyField(Pessoa)
    link_github = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo

class Escola(models.Model):
    nome = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    local = models.CharField(max_length=200)
    image = models.FileField(upload_to="uploads/")
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    image = models.FileField(upload_to="uploads/")
    
    def __str__(self):
        return self.nome

class Laboratorio(models.Model):
    nome = models.CharField(max_length=50)
    numero = models.IntegerField()
    link = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nome       

class Post(models.Model):
    autor = models.CharField(max_length=50)
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo

class Quiz(models.Model):
    nome = models.CharField(max_length=60)
    pontuacao = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Rede(models.Model):
    descricao = models.TextField(max_length=500)
    image = models.FileField(upload_to="uploads/")
    link = models.CharField(max_length=300)
    
    def __str__(self):
        return self.descricao

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)
    image = models.FileField(upload_to="uploads/")
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo    
from django.contrib import admin
from .models import Pessoa, Linguagem, Projeto, Cadeira, Escola, Interesse, Laboratorio, Post

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Linguagem)
admin.site.register(Projeto)
admin.site.register(Cadeira)
admin.site.register(Escola)
admin.site.register(Interesse)
admin.site.register(Laboratorio)
admin.site.register(Post)
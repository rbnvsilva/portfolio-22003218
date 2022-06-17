from django import forms
from django.forms import ModelForm
from .models import Post, Projeto, Cadeira, Tfc

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'       

class TfcForm(ModelForm):
    class Meta:
        model = Tfc
        fields = '__all__'    
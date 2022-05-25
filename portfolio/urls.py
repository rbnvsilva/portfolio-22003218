from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre_mim', views.sobre_mim_view, name='sobre_mim'),
    path('projetos', views.projetos_view, name='projetos'),
    path('pw', views.pw_view, name='pw'),
    path('blog', views.blog_view, name='blog'),
    path('contacto', views.contacto_view, name='contacto'),
]
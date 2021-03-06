from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre_mim', views.sobre_mim_view, name='sobre_mim'),
    path('criar_cadeira', views.criar_cadeira_view, name='criar_cadeira'),
    path('editar_cadeira/<int:cadeira_id>', views.editar_cadeira_view, name='editar_cadeira'),
    path('projetos', views.projetos_view, name='projetos'),
    path('criar_projeto', views.criar_projeto_view, name='criar_projeto'),
    path('editar_projeto/<int:projeto_id>', views.editar_projeto_view, name='editar_projeto'),
    path('criar_tfc', views.criar_tfc_view, name='criar_tfc'),
    path('editar_tfc/<int:tfc_id>', views.editar_tfc_view, name='editar_tfc'),
    path('pw', views.pw_view, name='pw'),
    path('blog', views.blog_view, name='blog'),
    path('criar_post', views.criar_post_view, name='criar_post'),
    path('editar_post/<int:post_id>', views.editar_post_view, name='editar_post'),
    path('sobre_website', views.sobre_website_view, name='sobre_website'),
    path('contacto', views.contacto_view, name='contacto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
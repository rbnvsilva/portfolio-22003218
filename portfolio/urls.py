from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre_mim', views.sobre_mim_view, name='sobre_mim'),
    path('projetos', views.projetos_view, name='projetos'),
    path('pw', views.pw_view, name='pw'),
    path('blog', views.blog_view, name='blog'),
    path('criar-post', views.criar_post_view, name='criar_post'),
    path('sobre_website', views.sobre_website_view, name='sobre_website'),
    path('contacto', views.contacto_view, name='contacto'),
    path('editar/<int:post_id>', views.editar_post_view, name='editar_post'),
    path('apagar/<int:post_id>', views.apagar_post_view, name='apagar_post'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
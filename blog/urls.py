from django.urls import path
from . import views

# aqui serão incluidas as urls dessa sessão 'blog' ex: /blog/postagem
urlpatterns = [
    path('', views.index)
]
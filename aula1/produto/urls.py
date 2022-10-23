from django.urls import path
from . import views

# aqui serão incluidas as urls dessa sessão 'produto' ex: /produto/celular
urlpatterns = [
    path('', views.metodo)
]
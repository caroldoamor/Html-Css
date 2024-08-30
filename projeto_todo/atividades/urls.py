from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.sucesso_view, name='sucesso'),
]

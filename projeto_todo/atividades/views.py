from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sucesso_view(request):
    return HttpResponse("Realizado com sucesso a atividade")

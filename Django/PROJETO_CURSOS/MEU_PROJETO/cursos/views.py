from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Curso, Aluno
from django.shortcuts import render #Para usar método post
from django.contrib.auth.decorators import login_required #Para garantir o login para acessar a view
from django.contrib import messages #Biblioteca de mensagens de navegador
# Create your views here.

def inicial_curso(request): #Cria a função a ser usada na rota do cursos.urls
    cursos = Curso.objects.all()
    if request.method == "POST":
        curso = request.POST.get("curso")
        CURSO = Curso.objects.filter(titulo__iexact=curso).first() #__iexact faz com que entenda maiusculo e minúsculo, mesmo que o nome do curso seja maiusculo e a busca seja minúscula
        if CURSO:
            return redirect(CURSO.link)           
        else: 
            return render(request, "registration/cursos.html",{"erro":"Curso não encontrado!", "cursos":cursos})
            
    return render(request, "registration/cursos.html", {"cursos":cursos})   #Tarefa para amanhã terminar o post dessa parte


@login_required
def painel(request):
    cursos_nome = Curso.objects.all()
    quantidade_alunos = Aluno.objects.count()

    if request.method == "POST":
        nome = request.POST.get("nome")
        aluno_nome = Aluno.objects.filter(nome__iexact=nome).first() #.first() retorna o objeto completo
         
        if aluno_nome:
             return render(request, "registration/aluno.html", {"aluno":aluno_nome})
        else:
            return render(request, "registration/painel.html", {"cursos":cursos_nome, "quantidade_alunos":quantidade_alunos, "erro":"Aluno não encontrado!"})
            

    
    return render(request, "registration/painel.html", {"cursos":cursos_nome, "quantidade_alunos":quantidade_alunos})

def curso_python(request):
    return render(request, "registration/curso_python.html")

def inicio(request):
    return render(request, "registration/inicio.html")

def curso_java(request):
    return render(request, "registration/curso_java.html")

def curso_django(request):
    return render(request, "registration/curso_django.html")

def curso_html(request):
    return render(request, "registration/curso_html.html")

#fazer mais um painel para professor
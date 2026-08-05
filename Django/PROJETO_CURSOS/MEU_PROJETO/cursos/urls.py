from django.urls import path
from . import views # . porque é da mesma pasta, importa view

urlpatterns = [  #Define a rota da função criada nas views
    path('', views.inicial_curso, name = "curso"),
    path('python/', views.curso_python, name="python"),
    path('java/', views.curso_java, name ="java"),
    path('django/', views.curso_django,name="django"),
    path('html/', views.curso_html,name="html")
]


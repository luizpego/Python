from django.contrib import admin
from .models import Professor, Curso, Aluno
# Register your models here.

admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Aluno)
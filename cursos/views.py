from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect 
from .models import Aulas, Cursos 
from usuarios.models import Usuario


def home(request):
    if request.session.get('usuario'):
        cursos = Cursos.objects.all()
        request_usuario = request.session.get('usuario')
        obj_usuario= Usuario.objects.get(id=request_usuario)
        return render(request, 'home.html', {'cursos': cursos, 'obj_usuario': obj_usuario})
    else:
        return redirect('/auth/login/?status=2')

def curso(request, id):
    cursoEscolhido = Cursos.objects.get(id = id)
    return render(request, 'curso.html', {'cursoEscolhido':cursoEscolhido})

    
def aula(request, id):
    if request.session.get('usuario'):
        aula = Aulas.objects.get(id = id)
        return render(request, 'aula.html', {'aula': aula})
    else:
        return redirect('/auth/login/?status=2')


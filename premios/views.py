from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect 
from .models import Premio 
from usuarios.models import Usuario


def home(request):
    if request.session.get('usuario'):
        premios = Premio.objects.all()
        request_usuario = request.session.get('usuario')
        obj_usuario= Usuario.objects.get(id=request_usuario)
        return render(request, 'home.html', {'premios': premios, 'obj_usuario': obj_usuario})
    else:
        return redirect('/auth/login/?status=2')

def premio(request, id):
    premioEscolhido = Premio.objects.get(id = id)
    return render(request, 'premio.html', {'premioEscolhido':premioEscolhido})

    

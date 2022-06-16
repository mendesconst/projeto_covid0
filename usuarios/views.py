from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, TokenCadastro
from cursos.models import Cursos
from django.shortcuts import redirect
import hashlib
import time

def cadastro(request):
    if request.session.get('usuario'):
        return sair(request)
    status=request.GET.get('status')
    return render(request,'cadastro.html', {'status': status})


def login(request):
    if request.session.get('usuario'):
        return redirect('/home')
    status = request.GET.get('status')
    return render(request,'login.html', {'status': status})
    
def valida_cadastro(request):
    nome = request.POST.get('nome')
    token=request.POST.get('token')
    senha=request.POST.get('senha')

    if not TokenCadastro.objects.filter(token_cadastro=token).exists():
        return redirect('/auth/cadastro?status=4')

    else:
        token_valido = TokenCadastro.objects.filter(token_cadastro=token)
        usuario_existe=Usuario.objects.filter(token_cadastro=token_valido[0])
    
    if len(senha) < 8 or len(senha) >12:
        return redirect('/auth/cadastro?status=1')

    if len(nome.strip()) == 0 or len(token.strip()) == 0:
        return redirect('/auth/cadastro?status=2')

    if len(usuario_existe) > 0:
        return redirect('/auth/cadastro?status=3')
    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario=Usuario(nome=nome,
                        senha=senha,
                        token_cadastro=token_valido[0])
        usuario.save()
        return redirect('/auth/cadastro?status=0')
    except:
        return HttpResponse('ERRO INTERNO DO SISTEMA, TENTE NOVAMENTE EM INSTANTES')

def curso_escolhido(request, id):
        cursoEscolhido = Cursos.objects.get(id = id)
        request_usuario = request.session.get('usuario')
        request_usuario = Usuario.objects.get(id=request_usuario)
        request_usuario.curso_selecionado = cursoEscolhido
        usuario=request_usuario
        usuario.save()
        time.sleep(5) 
        return sair(request) 

def valida_login(request):
    token=request.POST.get('token')
    senha=request.POST.get('senha')
    senha=hashlib.sha256(senha.encode()).hexdigest()
    token_valido = TokenCadastro.objects.filter(token_cadastro=token)
    usuario=Usuario.objects.filter(token_cadastro=token_valido[0])

    if len(usuario) ==0:
        return redirect('/auth/login?status=1')
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        time.sleep(3)
        return redirect('/home')


def sair(request):
    request.session.flush()
    return redirect('/auth/login')

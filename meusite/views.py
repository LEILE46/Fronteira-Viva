from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .models import PontoHistorico, HistoriaColaborativa, Cambio, PerfilUsuario
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    todos_pontos = PontoHistorico.objects.all()
    print(todos_pontos)
    context = {
        'culturas': todos_pontos.filter(categoria='Culturas'),
        'historias_locais': todos_pontos.filter(categoria='HISTORIA'),
        'roteiros': todos_pontos.filter(categoria='ROTEIRO'),
        'cambios': Cambio.objects.all().order_by('-melhor_cotacao'),
        'historias_usuarios': HistoriaColaborativa.objects.filter(aprovado=True),
        'agricultura': todos_pontos.filter(categoria='AGRICULTURA'),
        'trajetoria': todos_pontos.filter(categoria='TRAJETORIA'),
    }
    return render(request, 'home.html', context)


def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

      
        if User.objects.filter(username=nome).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return render(request, 'meusite/cadastro.html')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        login(request, user)
        
        messages.success(request, "Conta criada com sucesso! Bem-vindo ao Fronteira Viva.")
        return redirect('home')

    return render(request, 'cadastro.html')


@login_required
def publicar_historia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        
  
        HistoriaColaborativa.objects.create(
            autor=request.user,
            titulo=titulo,
            conteudo=conteudo,
            aprovado=False 
        )
   
        return render(request, 'publicar_sucesso.html')
    
    return render(request, 'publicar_historia.html')


def detalhe_ponto(request, pk):
    ponto = get_object_or_404(PontoHistorico, pk=pk)
    return render(request, 'detalhe_ponto.html', {'ponto': ponto})


@login_required
def salvar_preferencias(request):
    if request.method == 'POST':
        perfil = request.user.perfil
        perfil.tamanho_fonte = request.POST.get('fonte')
        perfil.alto_contraste = 'contraste' in request.POST
        perfil.save()
    return redirect('home')

from django.shortcuts import render, redirect

from .models import PontoHistorico, Cambio 

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        usuario_post = request.POST.get('username')
        senha_post = request.POST.get('password')


        user = authenticate(request, username=usuario_post, password=senha_post)

        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo de volta, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha incorretos. Tente novamente.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('home')
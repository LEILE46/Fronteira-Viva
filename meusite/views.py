from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import HistoriaColaborativa # Importa apenas o que existe

def home(request):
    # Agora a home busca apenas as histórias que você aprovou no Admin
    context = {
        'historias_usuarios': HistoriaColaborativa.objects.filter(aprovado=True),
    }
    return render(request, 'home.html', context)

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        if User.objects.filter(username=nome).exists():
            messages.error(request, "Este nome de usuário já está em uso.")
            return render(request, 'cadastro.html')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        login(request, user)
        
        messages.success(request, "Conta criada com sucesso! Bem-vindo.")
        return redirect('home')

    return render(request, 'cadastro.html')

@login_required
def publicar_historia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        
        # Cria a história no banco. Ela nasce com aprovado=False
        HistoriaColaborativa.objects.create(
            autor=request.user,
            titulo=titulo,
            conteudo=conteudo,
            aprovado=False 
        )
        
        messages.success(request, "Sua história foi enviada para análise do administrador!")
        return redirect('home')
    
    return redirect('home')

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
            messages.error(request, "Usuário ou senha incorretos.")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('home')
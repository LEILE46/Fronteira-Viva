from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PontoHistorico, HistoriaColaborativa, Cambio

def home(request):
    todos_pontos = PontoHistorico.objects.all()
    print(todos_pontos.filter(categoria='Historias'))
    context = {
        'culturas': todos_pontos.filter(categoria='CULTURAS'),
        'historias_locais': todos_pontos.filter(categoria='Historias'),
        'roteiros': todos_pontos.filter(categoria='ROTEIRO'),
        'cambios': Cambio.objects.all().order_by('-melhor_cotacao'),
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
            return render(request, 'cadastro.html')  # caminho correto

        user = User.objects.create_user(username=nome, email=email, password=senha)
        login(request, user)
        messages.success(request, "Conta criada com sucesso! Bem-vindo ao Fronteira Viva.")
        return redirect('home')  # nome da URL, não do template

    return render(request, 'cadastro.html')
# ====== PUBLICAR HISTÓRIA ======
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

        messages.success(request, "História enviada! Aguardando aprovação.")
        return render(request, 'publicar_sucesso.html')  # ou redirect para uma página de sucesso

    return render(request, 'publicar_historia.html')

# ====== DETALHE DO PONTO ======
def detalhe_ponto(request, pk):
    ponto = get_object_or_404(PontoHistorico, pk=pk)
    return render(request, 'detalhe_ponto.html', {'ponto': ponto})

# ====== LOGIN ======
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

# ====== LOGOUT ======
def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('home.html')
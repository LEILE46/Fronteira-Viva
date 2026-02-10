from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import PontoHistorico, HistoriaColaborativa, Cambio, PerfilUsuario


def home(request):
    pontos = PontoHistorico.objects.all()
    historias_aprovadas = HistoriaColaborativa.objects.filter(aprovado=True)
    cambios = Cambio.objects.all().order_by('-melhor_cotacao', '-ultima_atualizacao')    
    context = {
        'pontos': pontos,
        'historias': historias_aprovadas,
        'cambios': cambios,
    }
    return render(request, 'home.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
      
            PerfilUsuario.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})


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
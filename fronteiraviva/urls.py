from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from meusite import views  

urlpatterns = [
    # Caminho do Administrador
    path('admin/', admin.site.urls),

    # Página Inicial (Home)
    path('', views.home, name='home'),

    # Autenticação
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')), 

    # Histórias (Única funcionalidade ativa)
    path('publicar/', views.publicar_historia, name='publicar_historia'),
]

# Configuração para arquivos de mídia (imagens das histórias, se houver)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
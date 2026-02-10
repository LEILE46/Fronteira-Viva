"""
URL configuration for fronteiraviva project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from meusite import views  

urlpatterns = [
   
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

 
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('publicar/', views.publicar_historia, name='publicar_historia'),

    path('ponto/<int:pk>/', views.detalhe_ponto, name='detalhe_ponto'),

    path('preferencias/', views.salvar_preferencias, name='salvar_preferencias'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
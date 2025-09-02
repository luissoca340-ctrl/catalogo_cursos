"""
URL configuration for catalogo_curso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# catalogo_curso/urls.py
from django.contrib import admin
from django.urls import path, include
from cursos import views  # Importamos las vistas de la app cursos

urlpatterns = [
    path('admin/', admin.site.urls),  # Página de administración
    path('cursos/', include('cursos.urls')),  # Rutas de la app 'cursos'
    path('', views.home, name='home'),  # Ruta para la página principal (lista de cursos)
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cursos, name='listar_cursos'),
    path('crear/', views.crear_curso, name='crear_curso'),
    path('editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),
]


from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

# cursos/views.py
from django.shortcuts import render
from .models import Curso

def home(request):
    cursos = Curso.objects.all()  # Obtener todos los cursos
    return render(request, 'cursos/listar.html', {'cursos': cursos})


# Vista para listar los cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar.html', {'cursos': cursos})

# Vista para crear un nuevo curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/formulario.html', {'form': form})

# Vista para editar un curso
def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/formulario.html', {'form': form})

# Vista para eliminar un curso
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('listar_cursos')

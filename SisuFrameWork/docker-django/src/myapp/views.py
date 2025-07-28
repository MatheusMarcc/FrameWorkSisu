from django import get_version
from django.views.generic import TemplateView
from .tasks import show_hello_world


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = get_version()
        return context


# Views do CRUD de Curso

from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'curso/form.html', {'form': form, 'titulo': 'Novo Curso'})

def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/form.html', {'form': form, 'titulo': 'Editar Curso'})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'curso/confirm_delete.html', {'curso': curso})

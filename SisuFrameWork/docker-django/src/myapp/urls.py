
from django.urls import path
from .views import (
    curso_list, curso_create, curso_update, curso_delete
)

urlpatterns = [
    path('cursos/', curso_list, name='curso_list'),
    path('cursos/novo/', curso_create, name='curso_create'),
    path('cursos/<int:pk>/editar/', curso_update, name='curso_update'),
    path('cursos/<int:pk>/excluir/', curso_delete, name='curso_delete'),
]

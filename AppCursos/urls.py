from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="home"),
    path('ver_cursos', views.ver_cursos, name="cursos"),
    # path('alta_curso/<nombre>', views.alta_curso),
    path('alta_curso', views.curso_formulario),
    path('buscar_curso', views.buscar_curso, name="buscar_curso"),
    path('buscar', views.buscar),
    path('elimina_curso/<int:id>', views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path('alumnos', views.alumnos, name='alumnos'),
    path('nuevo_alumno', views.alumno_formulario, name="nuevo_alumno"),
    path('ver_alumnos', views.ver_alumnos, name='alumnos'),
    path('elimina_alumno/<int:id>', views.elimina_alumno, name="elimina_alumno"),
    path("editar_alumno/<int:id>" , views.editar_alumno , name="editar_alumno"),
    path('profesores', views.profesores, name='profesores'),
    path('nuevo_profesor', views.profesor_formulario, name="nuevo_profesor"),
    path('ver_profesores', views.ver_profesores, name='profesores'),
    path('elimina_profesor/<int:id>', views.elimina_profesor, name="elimina_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name="editar_profesor"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path('editarPerfil' , views.editarPerfil , name="EditarPerfil")
]


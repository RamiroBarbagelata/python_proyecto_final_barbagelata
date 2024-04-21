from django.shortcuts import render
from AppCursos.models import Curso, Alumno, Profesor, Avatar
from django.http import HttpResponse
from django.template import loader
from AppCursos.forms import Curso_formulario, Alumno_formulario, Profesor_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render (request, "padre.html")



#CURSOS

def curso_formulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html", {"url":avatares[0].imagen.url})

@login_required
def ver_cursos(request):
    # cursos = Curso.objects.all()
    # dicc = {"cursos": cursos}
    # plantilla = loader.get_template("cursos.html")
    # documento = plantilla.render(dicc)
    # return HttpResponse(documento)

    cursos = Curso.objects.all()   
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "cursos.html", {"url":avatares[0].imagen.url , "cursos": cursos })

def buscar_curso(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render( request , "buscar_curso.html" , {"url":avatares[0].imagen.url})
    # return render(request, "buscar_curso.html")

@login_required
def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        avatares = Avatar.objects.filter(user=request.user.id)
        return render( request , "resultado_busqueda.html" , {"url":avatares[0].imagen.url ,"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    
    
    
@login_required   
def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render (request, "cursos.html", {"cursos": curso, "url":avatares[0].imagen.url})

def editar(request , id):
    curso = Curso.objects.get(id=id)
    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            curso = Curso.objects.all()
            
            return render(request , "cursos.html" , {"cursos":curso})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso, "url":avatares[0].imagen.url})

# ALUMNOS
def alumnos(request):
    return render(request, "alumnos.html")
    

def nuevo_alumno(request, nombre_alumno, apellido_alumno, legajo_alumno):
    alumno = Alumno(nombre_alumno=nombre_alumno, apellido_alumno=apellido_alumno, legajo_alumno=legajo_alumno)
    alumno.save()
    texto = f"Se guardo en la Base de datos el Alumno: {alumno.nombre_alumno} {alumno.apellido_alumno} ({alumno.legajo_alumno})"
    return HttpResponse(texto)
    

@login_required
def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    # dicc = {"alumnos": alumnos}
    # plantilla = loader.get_template("alumnos.html")
    # documento = plantilla.render(dicc)
    
    # return HttpResponse(documento)
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "alumnos.html", {"url":avatares[0].imagen.url, "alumnos": alumnos})

def alumno_formulario(request):
    
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre_alumno = datos["nombre_alumno"], apellido_alumno = datos["apellido_alumno"], legajo_alumno = datos["legajo_alumno"])
            alumno.save()
            return render(request , "formulario_alumno.html")
            
    return render(request , "formulario_alumno.html")

def elimina_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno = Alumno.objects.all()
    
    return render (request, "alumnos.html", {"alumnos": alumno})

def editar_alumno(request , id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre_alumno = datos["nombre_alumno"]
            alumno.apellido_alumno = datos["apellido_alumno"]
            alumno.legajo_alumno = datos ["legajo_alumno"]
            alumno.save()
            alumno = Alumno.objects.all()
            
            return render(request , "alumnos.html" , {"alumnos":alumno})
    else:
        mi_formulario = Alumno_formulario(initial={"nombre_alumno":alumno.nombre_alumno , "apellido_alumno":alumno.apellido_alumno, "legajo_alumno":alumno.legajo_alumno})
    
    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno})

# PROFESORES
def profesores(request):
    # return render(request, "profesores.html")
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "profesores.html", {"url":avatares[0].imagen.url})

def nuevo_profesor(request, nombre_profesor, apellido_profesor, materia_profesor, legajo_profesor):
    profesor = Profesor(nombre_profesor=nombre_profesor, apellido_profesor=apellido_profesor, materia_profesor=materia_profesor, legajo_profesor=legajo_profesor)
    profesor.save()
    texto = f"Se guardo en la Base de datos el Profesor: {profesor.nombre_profesor} {profesor.apellido_profesor} {profesor.materia_profesor} ({profesor.legajo_profesor})"
    return HttpResponse(texto)

@login_required
def ver_profesores(request):
    profesores = Profesor.objects.all()
    # dicc = {"profesores": profesores}
    # plantilla = loader.get_template("profesores.html")
    # documento = plantilla.render(dicc)
    
    # return HttpResponse(documento)
    
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "profesores.html", {"url":avatares[0].imagen.url, "profesores": profesores})

def profesor_formulario(request):
    
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor(nombre_profesor = datos["nombre_profesor"], apellido_profesor = datos["apellido_profesor"], materia_profesor = datos["materia_profesor"], legajo_profesor = datos["legajo_profesor"])
            profesor.save()
            return render(request , "formulario_profesor.html")
            
    return render(request , "formulario_profesor.html") 

def elimina_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor = Profesor.objects.all()
    
    return render (request, "profesores.html", {"profesores": profesor})

def editar_profesor(request , id):
    profesor = Profesor.objects.get(id=id)
    avatares = Avatar.objects.filter(user=request.user.id)
    
    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre_profesor = datos["nombre_profesor"]
            profesor.apellido_profesor = datos["apellido_profesor"]
            profesor.materia_profesor = datos["materia_profesor"]
            profesor.legajo_profesor = datos ["legajo_profesor"]
            profesor.save()
            profesor = Profesor.objects.all()
            
            return render(request , "profesores.html" , {"profesores":profesor})
    else:
        mi_formulario = Profesor_formulario(initial={"nombre_profesor":profesor.nombre_profesor , "apellido_profesor":profesor.apellido_profesor, "materia_profesor":profesor.materia_profesor, "legajo_profesor":profesor.legajo_profesor})
    
    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor, "url":avatares[0].imagen.url})


# LOGIN

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contrasena)
            
            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render (request, "inicio.html", {"url":avatares[0].imagen.url, "mensaje": f"Bienvenido/a {usuario}", "usuario": usuario})
            else:
                return HttpResponse(f"Usuario no encontrado")
            
        else: 
            return HttpResponse(f"FORM INCORRECTO {form}")
    
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario Creado")
    
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})


def editarPerfil(request):
    usuario = request.user
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render (request, "inicio.html")

    else:
        mi_formulario = UserEditForm(initial={"email":usuario.email})
    
    return render (request , "editar_perfil.html", {"miFormulario":mi_formulario, "usuario":usuario, "url":avatares[0].imagen.url})


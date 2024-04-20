from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"
    
class Alumno (models.Model):
    nombre_alumno = models.CharField(max_length=40)
    apellido_alumno = models.CharField(max_length=40)
    legajo_alumno = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre_alumno} Apellido: {self.apellido_alumno} Legajo: {self.legajo_alumno} "
    
class Profesor (models.Model):
    nombre_profesor = models.CharField(max_length=40)
    apellido_profesor = models.CharField(max_length=40)
    materia_profesor = models.CharField(max_length=40)
    legajo_profesor = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre_profesor} Apellido: {self.apellido_profesor} Materia: {self.materia_profesor} Legajo: {self.legajo_profesor} "
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)
    
    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"
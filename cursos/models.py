from django.db import models

class Curso(models.Model):
    curso = models.CharField(max_length=100)   
    duracion = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    dificultad = models.CharField(max_length=50)

    def __str__(self):
        return self.curso   

from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length= 200)
    
    def __str__(self) -> str:
        return self.name


"Crear wed"
class Task (models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    project = models.ForeignKey (Project, on_delete=models.CASCADE) #tiene relacion con otra tabla, en este caso, Project
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title + ' - ' + self.project.name

"descargar Python"

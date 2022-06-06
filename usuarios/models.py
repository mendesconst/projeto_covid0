from django.db import models
from cursos.models import Cursos 

class Usuario(models.Model):
    nome=models.CharField(max_length=50)
    email=models.EmailField()
    senha=models.CharField(max_length=64)
    curso_selecionado=models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

        

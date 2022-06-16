from django.db import models
from cursos.models import Cursos 

class TokenCadastro(models.Model):
    token_cadastro=models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.token_cadastro

class Usuario(models.Model):
    nome=models.CharField(max_length=50)
    senha=models.CharField(max_length=64)
    curso_selecionado=models.ForeignKey(Cursos, on_delete=models.DO_NOTHING, null=True)
    token_cadastro=models.OneToOneField(TokenCadastro, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.nome


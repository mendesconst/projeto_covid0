from django.db import models

class Premio(models.Model):
    nome_premio = models.CharField(max_length = 100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to = "thumb_premios")

    def __str__(self) -> str:
        return self.nome_premio



from django.db import models

class Documento(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    versao = models.BigIntegerField(default=0)
    conteudo = models.TextField(blank=True)
    

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

        def __str__(self):
            return self.__all__
from django.db import models

# Create your models here.
class Student(models.Model):
    nome = models.CharField(max_length=80)
    cr = models.IntegerField()

    def __str__(self) -> str:
        return f"Nome: {self.nome} - CR: {self.cr}"
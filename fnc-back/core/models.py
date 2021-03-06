from django.db import models

class Member(models.Model):
    nome = models.CharField(max_length=100)
    exame = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome + " " + self.exame

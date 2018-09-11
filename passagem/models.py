from django.db import models

# Create your models here.
class Hospital(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

class Leito(models.Model):
    numero = models.SmallIntegerField()
    status = models.CharField(max_length=2, default='V')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero

class Paciente(models.Model):
    nome = models.CharField(max_length=250)
    leito = models.ForeignKey(Leito, on_delete=models.DO_NOTHING)
    pesoNasc = models.IntegerField()

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=250)
    crm = models.CharField(max_length=8)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.nome



from django.db import models

# Create your models here.
class Hospital(models.Model):
    nome = models.CharField(max_length=250)
    alias = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class Leito(models.Model):
    numero = models.SmallIntegerField()
    categoria = models.SmallIntegerField(default=0) #0 - UTIN 1 - MR 2 - CANGURU
    status = models.CharField(max_length=2, default='V')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return "Leito " + str(self.numero) + " - " + str(self.hospital) + ' Cat(' + str(self.categoria) + ')'


class Paciente(models.Model):
    nome = models.CharField(max_length=250)
    leito = models.ForeignKey(Leito, on_delete=models.DO_NOTHING)
    pesoNasc = models.IntegerField()
    dataNasc = models.DateField()

    def __str__(self):
        return self.nome + '(Leito ' + str(self.leito) + ')'


class Medico(models.Model):
    nome = models.CharField(max_length=250)
    crm = models.CharField(max_length=8)
    user = models.CharField(max_length=50)



class HospMed(models.Model):
    hospId = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    medId = models.ForeignKey(Medico, on_delete=models.CASCADE)


class Anotacao(models.Model):
    medId = models.ForeignKey(Medico, on_delete=models.CASCADE)
    pacId = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    dataHora = models.DateTimeField()
    idade = models.SmallIntegerField()
    igc = models.CharField(max_length=20)
    pesoAtual = models.IntegerField()
    diagn = models.CharField(max_length=200)
    dieta = models.CharField(max_length=100)
    acesso = models.CharField(max_length=2, default='N') #Nenhum, Periférico, Punção, Dissecção, PIcc
    atbMed = models.CharField(max_length=100)
    ventilacao = models.CharField(max_length=2, default='A') #Ar ambiente, CPAP, VNI, VM
    fototerapia = models.BooleanField(default=False)
    exames = models.CharField(max_length=500)
    conduta = models.CharField(max_length=500)

    class Meta:
        ordering = ('-dataHora', )
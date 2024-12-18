from loja.models import *

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    Nome = models.CharField(null=False, max_length=100)
    CPF = models.CharField(null=False, max_length=11, unique=True)
    Telefone_celular = models.CharField(null=False, max_length=11)

    def __str__(self):
        return f'{self.Nome}'
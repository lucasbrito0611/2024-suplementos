from loja.models import *

class Cartao(models.Model):
    TIPOS = [
        ('debito', 'Débito'),
        ('credito', 'Crédito'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(null=False, max_length=100)
    nometitular = models.CharField(null=False, max_length=100)
    numero = models.CharField(null=False, max_length=100)
    bandeira = models.CharField(null=False, max_length=50)
    tipo = models.CharField(max_length=10, choices=TIPOS)

    def __str__(self):
        return f'{self.nome} - {self.cliente}'
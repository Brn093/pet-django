from django.db import models
from django.contrib.auth.models import User

# Criando as tabelas
class Pet(models.Model):
    
    cidade = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    data_inicio = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='pet', blank=True, null=True)
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)   # o usuário cadastra o pet, CASCADE deleta em cascata
    
    # Retornará uma string ao invocar o Pet
    def __str__(self):
        return str(self.id)
    
    # Inserindo o nome da tabela no banco
    class Meta:
        db_table = 'pet'
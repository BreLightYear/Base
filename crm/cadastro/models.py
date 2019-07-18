from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Digite seu nome', max_length=15)
    ultimo_nome = models.CharField('Digite seu ultimo nome', max_length=25)
    endereco = models.CharField('Digite seu endereço',  max_length=50)
    idade = models.IntegerField()
    email = models.EmailField(unique = True, max_length=254)
    telefone = models.CharField('Digite seu numero de telefone', max_length=50)

    class Meta:
        ordering = ['nome']
        verbose_name =  (u'nome')
        verbose_name_plural = (u'nomes')

        def __unicode__(self):
            return self.nome


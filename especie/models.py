#!-*- coding: utf-8 -*-
import os
from django.db import models

from familia.models import Familia


class Configuracoes():
    u""" Classe para definição de tipos gerais """
	
    TIPOS_UMIDADE = (
        ('UC', 'Ultra seco'),
        ('S', 'Seco'),
        ('M', 'Moderado'),
        ('U', 'Úmido'),
        ('UM', 'Ultra úmido'),
    )
	
    TIPOS_PORTE = (
        ('AQ', 'Aquática'),
		('EP', 'Erva pequena'),
        ('EM', 'Erva média'),
        ('EG', 'Erva grande'),
        ('TP', 'Trepadeira'),
        ('AB', 'Arbusto'),
        ('AP', 'Árvore pequena'),
        ('AM', 'Árvore média'),
        ('AG', 'Árvore grande'),
        ('NA', 'Outro / não especificado'),
    )

    TIPOS_SOLO = (
        ('AE', 'Arenoso'),
        ('AE', 'Areno-siltoso'),
        ('SL', 'Siltoso'),
        ('AG', 'Argiloso'),
        ('AS', 'Argilo-siltoso'),
        ('AE', 'Areno-argiloso'),
        ('RC', 'Rochoso'),
        ('HU', 'Húmico'),
        ('OU', 'Outros')
    )

    NUMBER_RANGE = tuple((n, n) for n in range(10))
	
    TIPOS_ESTRATO = (
        ('B', 'Baixo'),
        ('M', 'Médio'),
        ('A', 'Alto/dossel'),
        ('E', 'Emergente'),
	)
	
    TIPOS_SUCESSAO = (
        ('CO', 'Colonizadora'),
        ('PI', 'Pioneiras'),
        ('SI', 'Secundárias iniciais'),
		('ST', 'Secundárias tardias'),
        ('CL', 'Clímax'),
	)
	
    TIPOS_CLIMA = (
        ('TRU', 'Tropical úmido'),
        ('TRS', 'Tropical seco'),
        ('STS', 'Sub tropical seco'),
		('STU', 'Sub tropical úmido'),
        ('TEU', 'Temperado úmido'),
        ('TES', 'Temperado seco')
    )

    TIPOS_BIOMA = (
        ('CE', 'Cerrado'),
        ('MA', 'Mata atlântica'),
        ('PA', 'Pampa'),
        ('AM', 'Amazônico'),
        ('PA', 'Pantanal')
    )

    TIPOS_DECLIVIDADE = (
        ('PL', 'Plano'),
        ('BA', 'Baixada'),
        ('EA', 'Encosta acentuada'),
        ('ES', 'Encosta suave')
    )

    FASES = (
        (0, 'Emergência'),
        (1, 'Desenvolvimento juvenil'),
        (2, 'Desenvolvimento pleno'),
        (3, 'Semi-caducidade'),
        (4, 'Caducidade'),
        (-1, 'Poda juvenil'),
        (-2, 'Poda severa'),
    )

    UNIDADE_TEMPO_VIDA = (
        ('D', 'Dias'),
        ('M', 'Meses'),
        ('A', 'Anos')
    )


def get_image_path(instance, filename):
	return os.path.join('images', str(instance.id), filename)

	
class Especie(models.Model):
    u""" Classe para definição de espécies """

    nome_cientifico  = models.CharField('nome_cientifico' , max_length=255, blank=True)
    nomes_populares  = models.CharField('nomes_populares', max_length=1000)
    familia          = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    temperatura_min  = models.IntegerField('temperatura_min', blank=True, null=True)
    temperatura_max  = models.IntegerField('temperatura_max', blank=True, null=True)
    inicio_colheita  = models.IntegerField('inicio_colheita', blank=True, null=True)
    porte            = models.CharField('porte', max_length=2, choices=Configuracoes.TIPOS_PORTE, blank=True)
    tempo_vida       = models.IntegerField('tempo_vida', blank=True, null=True)
    unidade_tempo_vida = models.CharField('unidade_tempo_vida', max_length=1, choices=Configuracoes.UNIDADE_TEMPO_VIDA, default="M")
    umidade          = models.CharField('umidade', max_length=2, choices=Configuracoes.TIPOS_UMIDADE, blank=True)
    exigencia_solo   = models.CharField('exigencia_solo', max_length=2, choices=Configuracoes.TIPOS_SOLO, blank=True)
    tolerancia_poda  = models.CharField('tolerancia_poda', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    exigencia_sol    = models.CharField('exigencia_sol', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    inicio_colheita  = models.CharField('inicio_colheita', max_length=5, blank=True)
    estrato          = models.CharField('estrato', max_length=2, choices=Configuracoes.TIPOS_ESTRATO, blank=True)
    sucessao         = models.CharField('sucessao', max_length=2, choices=Configuracoes.TIPOS_SUCESSAO, blank=True)
    imagem           = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	
    def __str__(self):
        return self.nomes_populares + " (" + self.nome_cientifico + ")"


class Variedade(models.Model):
    u""" Classe para definição de variedades de espécies """
	
    nome             = models.CharField('nome' , max_length=255, blank=True)
    descricao        = models.TextField('descricao', blank=True)
    exigencia_solo   = models.CharField('exigencia_solo', max_length=2, choices=Configuracoes.TIPOS_SOLO, blank=True)
    tolerancia_poda  = models.CharField('tolerancia_poda', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    exigencia_sol    = models.CharField('exigencia_sol', max_length=2, choices=Configuracoes.NUMBER_RANGE, blank=True)
    inicio_colheita  = models.CharField('inicio_colheita', max_length=5, blank=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, null=True, blank=False)
	
    def __str__(self):
        return self.nome

	
class Interacao(models.Model):
	u"""
	Interação entre especies
	"""

	TIPOS_INTERACAO = (
		('Sinergia', 'Sinergia'),
		('Alelopatia mútua', 'Alelopatia mútua'),
		('Alelopatia própria', 'Alelopatia própria'),
		('Alelopatia alheia', 'Alelopatia alheia'),
	)

	tipo_interacao  = models.CharField('tipo_interacao', max_length=10, choices=TIPOS_INTERACAO, blank=True)
	familia_a       = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='familia_a', null=True, blank=True)
	familia_b       = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='familia_b', null=True, blank=True)
	especie_a       = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='especie_a', null=True, blank=True)
	especie_b       = models.ForeignKey(Especie, on_delete=models.CASCADE, related_name='especie_b', null=True, blank=True)
	intensidade     = models.IntegerField('intensidade', choices=Configuracoes.NUMBER_RANGE, null=True, blank=True)
	descricao       = models.TextField('descricao', null=True, blank=True)
	
	def __str__(self):
		
		rotulo = ''
		
		if self.familia_a != None:
		 	rotulo += '(' + self.familia_a.nome + ')'
		if self.familia_a != None and self.familia_b != None:
			rotulo += ' => '
		else:
			rotulo += '_ '		
		if self.familia_b != None:
		 	rotulo += '(' + self.familia_b.nome + ') '
		
		rotulo += self.especie_a.nomes_populares + ' => ' + self.especie_b.nomes_populares + ' ( ' + self.tipo_interacao + ')'

		return rotulo

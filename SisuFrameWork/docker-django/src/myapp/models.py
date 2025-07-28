from django.db import models
from django.contrib.auth.models import User
from django.db import models, transaction

class Curso(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Edicao(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    def saveMany(self, nested_data):
        """
        Salva a edição e todos os EdicaoCurso associados.
        """
        from .models import EdicaoCurso, Curso  # Importação interna para evitar problemas circulares

        with transaction.atomic():
            self.save()  # Salva a edição

            # Remove registros antigos se for update
            EdicaoCurso.objects.filter(edicao=self).delete()

            for data in nested_data.get('cursos', []):
                curso_id = data.get('curso_id')
                try:
                    curso = Curso.objects.get(pk=curso_id)
                except Curso.DoesNotExist:
                    continue  # ignora se curso inválido

                edicao_curso = EdicaoCurso(
                    edicao=self,
                    curso=curso,
                    vagas_ac=data.get('vagas_ac', 0) or 0,
                    vagas_ppi_br=data.get('vagas_ppi_br', 0) or 0,
                    vagas_publica_br=data.get('vagas_publica_br', 0) or 0,
                    vagas_ppi_publica=data.get('vagas_ppi_publica', 0) or 0,
                    vagas_publica=data.get('vagas_publica', 0) or 0,
                    vagas_deficientes=data.get('vagas_deficientes', 0) or 0,
                )
                edicao_curso.save()


class EdicaoCurso(models.Model):
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    vagas_ac = models.IntegerField(default=0)
    vagas_ppi_br = models.IntegerField(default=0)
    vagas_publica_br = models.IntegerField(default=0)
    vagas_ppi_publica = models.IntegerField(default=0)
    vagas_publica = models.IntegerField(default=0)
    vagas_deficientes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.edicao.nome} - {self.curso.nome}"


class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    categoria = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.nome} ({self.categoria})"

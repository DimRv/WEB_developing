from django.db import models


class Functions(models.Model):
    function = models.CharField("Функция", max_length=30, unique=True)
    description = models.CharField("Описание", max_length=200)

    class Meta:
        ordering = ["function"]


class Syntax(models.Model):
    func_id = models.ForeignKey(Functions, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)


class Params(models.Model):
    parameter = models.CharField("Параметр", max_length=30, unique=True)
    default_value = models.CharField("Значение", max_length=30, unique=True)
    description = models.CharField("Описание", max_length=200)
    syntax_id = models.ManyToManyField(Syntax, through="SyntaxParams")


    class Meta:
        ordering = ["parameter"]


class SyntaxParams(models.Model):
    syntax_id = models.ForeignKey(Syntax, on_delete=models.CASCADE)
    parameter_id = models.ForeignKey(Params, on_delete=models.CASCADE)
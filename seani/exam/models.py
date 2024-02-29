from django.db import models

class Stage(models.Model):
    stage=models.IntegerField(
        verbose_name='Etapa',
    )
    application_date= models.DateField(
        verbose_name='Fecha de Aplicacion',
    )

def month(self):
    months=['enero','febrero','marzo','abril','mayo','junio','julio',
            'agosto','septiembre','octubre','noviembre','diciembre']
    return months[self.application_date.month-1]
month.short_description ='Año'

def year(self):
    return self.application_date.year
year.short_description ='Año'

def __str__(self):
    return f"{ self.stage } - { self.month()} { self.year()}"

class Meta:
    verbose_name='Etapa'
    verbose_name_plural="etapas"
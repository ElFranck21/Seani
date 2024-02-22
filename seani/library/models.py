from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Module(models.Model):
    name= models.CharField(
        verbose_name='Nombre del modulo',
        max_length=30)
    description= models.CharField(
        verbose_name='Descripcion del modulo',
        max_length= 150)
    def num_questions(self):
        return self.question_set.count()
    num_questions.short_description='Numero de Preguntas'

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='modulo'
        verbose_name_plural='modulos'

class Question(models.Model):
    module=models.ForeignKey(Module, on_delete=models.CASCADE)
    question_text= models.CharField(
        null=True, blank=True,
        verbose_name='Texto de la pregunta',
        max_length=255)
  ##  question_image= models.ImageField(
    ##    null=True, blank=True,
      ##  verbose_name='Imagen de la pregunta',
        ##upload_to='questions')
    question_image=CloudinaryField(
        null=True, blank=True,
        verbose_name='Imagen de la pregunta',
        resource_type='image',
        folder='questions',
    )
    answer1= models.CharField(
        verbose_name='Respuesta A',
        max_length=150)
    answer2= models.CharField(
        verbose_name='Respuesta B',
        max_length=150)
    answer3= models.CharField(
        null=True, blank=True,
        verbose_name='Respuesta C',
        max_length=150)
    answer4= models.CharField(
        null=True, blank=True,
        verbose_name='Respuesta D',
        max_length=150)
    correct= models.CharField(
        verbose_name='Respuesta correcta',
        max_length=190)
    
    def __str__(self):
        return f"{self.module} Pregunta {self.id}"
    
    class Meta:
        verbose_name='Pregunta'
        verbose_name_plural='Preguntas'
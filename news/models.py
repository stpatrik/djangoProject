from django.db import models

# Create your models here.
class Articles (models.Model):
    title = models. CharField('Назва', max_length=70)
    anons = models. CharField('Анонс', max_length=350)
    full_text = models.TextField('Стаття')
    date = models. DateTimeField('Дата публикації')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

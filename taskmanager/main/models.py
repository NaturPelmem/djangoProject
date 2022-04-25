from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абрамов Сергей Андреевич'
        verbose_name_plural = 'Абрамов С.А.'

class Tasks(models.Model):
    title = models.CharField('Название', max_length=50)
    text = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аминова Анастасия Сергеевна'
        verbose_name_plural = 'Аминова А.С.'
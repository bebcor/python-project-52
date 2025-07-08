from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label 

User = get_user_model()

class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    author = models.ForeignKey(
        User,
        related_name='authored_tasks',
        on_delete=models.PROTECT,
        verbose_name='Автор'
    )
    executor = models.ForeignKey(
        User,
        related_name='assigned_tasks',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Исполнитель'
    )
    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        verbose_name='Метки',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name



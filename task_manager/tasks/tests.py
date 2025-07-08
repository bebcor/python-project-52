from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Task
from statuses.models import Status
from labels.models import Label
from .filters import TaskFilter

User = get_user_model()

class TaskFilterTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')
        self.status1 = Status.objects.create(name='Новый')
        self.status2 = Status.objects.create(name='В работе')
        self.label1 = Label.objects.create(name='Баг')
        self.label2 = Label.objects.create(name='Фича')
        
        self.task1 = Task.objects.create(
            name='Задача 1',
            status=self.status1,
            author=self.user1,
            executor=self.user1
        )
        self.task1.labels.add(self.label1)
        
        self.task2 = Task.objects.create(
            name='Задача 2',
            status=self.status2,
            author=self.user2,
            executor=self.user2
        )
        self.task2.labels.add(self.label2)

    def test_filter_by_status(self):
        request = self.factory.get('/tasks/?status=' + str(self.status1.id))
        request.user = self.user1
        task_filter = TaskFilter(request.GET, queryset=Task.objects.all(), request=request)
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_filter_by_executor(self):
        request = self.factory.get('/tasks/?executor=' + str(self.user1.id))
        request.user = self.user1
        task_filter = TaskFilter(request.GET, queryset=Task.objects.all(), request=request)
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_filter_by_label(self):
        request = self.factory.get('/tasks/?labels=' + str(self.label1.id))
        request.user = self.user1
        task_filter = TaskFilter(request.GET, queryset=Task.objects.all(), request=request)
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_filter_self_tasks(self):
        request = self.factory.get('/tasks/?self_tasks=on'))
        request.user = self.user1
        task_filter = TaskFilter(request.GET, queryset=Task.objects.all(), request=request)
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_filter_combination(self):
        request = self.factory.get(f'/tasks/?status={self.status1.id}&executor={self.user1.id}&labels={self.label1.id}&self_tasks=on')
        request.user = self.user1
        task_filter = TaskFilter(request.GET, queryset=Task.objects.all(), request=request)
        self.assertEqual(task_filter.qs.count(), 1)
        self.assertEqual(task_filter.qs.first(), self.task1)

    def test_no_filter(self):
        request = self.factory.get('/tasks/')
        request.user = self.user1
        task_filter = TaskFilter(request.GET, queryset=Task.objects.all(), request=request)
        self.assertEqual(task_filter.qs.count(), 2)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status 

User = get_user_model()

class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username='user1', password='testpass123')
        cls.user2 = User.objects.create_user(username='user2', password='testpass456')
        cls.user_with_task = User.objects.create_user(username='task_user', password='taskpass')
        
        cls.status = Status.objects.create(name='Test Status')
        cls.task = Task.objects.create(
            name='Test Task', 
            description='Task description',
            status=cls.status,
            author=cls.user_with_task
        )

    def test_user_update_permission(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(
            reverse('user_update', kwargs={'pk': self.user2.pk})
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users_list'))
        
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertIn('У вас нет прав', messages[0].message)

    def test_user_delete_with_tasks(self):
        Task.objects.create(
            name='Test Task', 
            description='Task description',
            status=Status.objects.create(name="Test Status"),
            author=self.user_with_task
        )
        
        self.client.login(username='task_user', password='taskpass')
        
        response = self.client.post(
            reverse('user_delete', kwargs={'pk': self.user_with_task.pk}),
            follow=True
        )
        
        self.assertContains(response, 'Невозможно удалить пользователя')

    def test_user_delete_without_tasks(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.post(
            reverse('user_delete', kwargs={'pk': self.user1.pk}),
            follow=True
        )
        
        self.assertContains(response, 'Пользователь успешно удален')
        self.assertFalse(User.objects.filter(pk=self.user1.pk).exists())

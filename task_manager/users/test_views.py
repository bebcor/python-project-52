from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()


class UserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            username='user1',
            password='testpass123'
        )
        cls.user2 = User.objects.create_user(
            username='user2',
            password='testpass123'
        )
        cls.user_with_task = User.objects.create_user(
            username='task_user',
            password='taskpass'
        )
        
        cls.status = Status.objects.create(name="Test Status")
        
        cls.task = Task.objects.create(
            name="Test Task",
            description="Test Description",
            status=cls.status,
            author=cls.user_with_task,
            executor=cls.user1
        )

    def setUp(self):
        self.client.logout()

    def test_user_update_permission(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(
            reverse('user_update', kwargs={'pk': self.user2.pk})
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users_list'))
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'У вас нет прав для изменения другого пользователя.')

    def test_user_delete_with_tasks(self):
        self.client.login(username='task_user', password='taskpass')
        
        response = self.client.post(
            reverse('user_delete', kwargs={'pk': self.user_with_task.pk}),
            follow=True
        )
        
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Невозможно удалить пользователя, потому что он связан с задачей'
        )
    

def test_user_delete_without_tasks(self):
    self.client.login(username='user1', password='testpass123')
    response = self.client.post(
        reverse('user_delete', kwargs={'pk': self.user1.pk}),
        follow=True
    )
    
    messages = list(response.context['messages'])
    self.assertEqual(len(messages), 1)
    self.assertEqual(str(messages[0]), 'Пользователь успешно удален')
    
    self.assertContains(response, 'Пользователь успешно удален')
    
    self.assertFalse(User.objects.filter(pk=self.user1.pk).exists())

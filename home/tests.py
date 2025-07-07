from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')
    
    def test_user_update_permission(self):
        self.client.login(username='user1', password='testpass')
        response = self.client.get(reverse('user_update', args=[self.user2.id]))
        self.assertEqual(response.status_code, 403)
    
    def test_user_delete_with_tasks(self):
        from tasks.models import Task
        from statuses.models import Status
        status = Status.objects.create(name='Test Status')
        task = Task.objects.create(
            name='Test Task',
            status=status,
            author=self.user1
        )
        
        self.client.login(username='user1', password='testpass')
        response = self.client.post(reverse('user_delete', args=[self.user1.id]))
        self.assertContains(response, 'Невозможно удалить пользователя')

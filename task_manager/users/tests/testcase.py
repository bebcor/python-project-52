from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    fixtures = ['test_users.json']  

    def setUp(self):
        self.user1 = User.objects.get(id=1)
        self.user2 = User.objects.get(id=2)
        self.user3 = User.objects.get(id=3)
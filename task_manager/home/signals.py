from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_migrate)
def create_initial_users(sender, **kwargs):
    if sender.name == 'home' and User.objects.count() == 0:
        User.objects.create_user(username='user1', password='password1')
        User.objects.create_user(username='user2', password='password2')
        User.objects.create_user(username='user3', password='password3')
        print("Created initial users")
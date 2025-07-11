from django.db import migrations

def create_initial_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    
    User.objects.create_user(username='user10', password='pass10')
    User.objects.create_user(username='user20', password='pass20')
    User.objects.create_user(username='user30', password='pass30')

class Migration(migrations.Migration):
    dependencies = [
    ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_initial_users),
    ]

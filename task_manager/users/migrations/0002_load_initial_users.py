from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_users(apps, schema_editor):
    User = apps.get_model('users', 'User')
    users = [
        {
            'username': 'john_snow',
            'password': make_password('Stark123'),
            'first_name': 'John',
            'last_name': 'Snow'
        },
        {
            'username': 'daenerys_t',
            'password': make_password('Dracarys123'),
            'first_name': 'Daenerys',
            'last_name': 'Targaryen'
        },
        {
            'username': 'simon_show',
            'password': make_password('Wine123'),
            'first_name': 'Simon',
            'last_name': 'Show'
        }
    ]
    
    for user_data in users:
        User.objects.create(**user_data)

class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]

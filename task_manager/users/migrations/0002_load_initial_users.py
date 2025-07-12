from django.db import migrations

def load_users(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "test_users.json")

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_users),
    ]

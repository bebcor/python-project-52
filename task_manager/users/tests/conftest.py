import pytest
from django.contrib.auth import get_user_model

@pytest.fixture(autouse=True)
def load_users(db):
    User = get_user_model()
    users = [
        User(
            username='john_snow',
            first_name='John',
            last_name='Snow',
            password='Stark123' 
        ),
        User(
            username='daenerys_t',
            first_name='Daenerys',
            last_name='Targaryen',
            password='Mira234'
        ),
        User(
            username='simon_show',
            first_name='Simon',
            last_name='Show',
            password='Simon134'
        )
    ]
    User.objects.bulk_create(users)
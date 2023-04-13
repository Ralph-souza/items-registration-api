import uuid

from django.utils import timezone
from factory.django import DjangoModelFactory

from apps.user_api.models import UserModel


class UserFactory(DjangoModelFactory):
    user = str(uuid.uuid4())
    user_name = "fake name"
    user_email = "fake_email@test.com"
    user_password = "fake_user_password"
    created_at = timezone.now()

    class Meta:
        model = UserModel

import pytest
from django.test import TestCase

from apps.user_api.models import UserModel

# from django.utils import timezone
# from django.core.urlresolvers import reverse


pytestmark = pytest.mark.django_db


class TestUserModel(TestCase):
    @staticmethod
    def create_user(user_payload):
        return UserModel.objects.create(user_payload)

    def test_user_creation(self, user_payload):
        user = self.create_user(user_payload)
        self.assertTrue(isinstance(user, UserModel))
        self.assertEqual(user.__unicode__(), user.user_name)

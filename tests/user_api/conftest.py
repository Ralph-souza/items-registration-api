import pytest

from .factories import UserFactory


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def user_payload():
    return {
        "user_name": "Some user",
        "user_email": "some_user_email@test.com",
        "user_password": "some_user_password",
    }


@pytest.fixture
def user_invalid_payload():
    return {
        "user_name": None,
        "user_email": "some_user_email@test.com",
        "user_password": "some_user_password",
    }

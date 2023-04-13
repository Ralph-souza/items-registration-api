import pytest

from .factories import LoanerFactory


@pytest.fixture
def loaner():
    return LoanerFactory()


@pytest.fixture
def loaner_payload():
    return {
        "loaner_name": "Some loaner",
        "loaner_email": "some_loaner_email@test.com",
        "loaner_phone": "+55 (11)9 9999-9999",
    }


@pytest.fixture
def loaner_invalid_payload():
    return {
        "loaner_name": None,
        "loaner_email": "some_loaner_email@test.com",
        "loaner_phone": "+55 (11)9 9999-9999",
    }

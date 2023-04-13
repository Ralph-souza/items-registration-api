from django.test import TestCase

from apps.loaner_api.models import LoanerModel


class TestLoanerModel(TestCase):
    @staticmethod
    def create_loaner(loaner_payload):
        return LoanerModel.objects.create(loaner_payload)

    def test_loaner_creation(self, loaner_payload):
        loaner = self.create_loaner(loaner_payload)
        self.assertTrue(isinstance(loaner, LoanerModel))
        self.assertEqual(loaner.__unicode__(), loaner.loaner_name)

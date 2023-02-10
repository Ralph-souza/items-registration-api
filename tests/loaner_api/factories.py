import uuid

from factory.django import DjangoModelFactory
from django.utils import timezone

from apps.loaner_api.models import LoanerModel


class LoanerFactory(DjangoModelFactory):
    loaner = str(uuid.uuid4())
    loaner_name = "fake name"
    loaner_email = "fake_email@test.com"
    loaner_phone = "+55 (11)9 9999-9999"
    loaned_video_item = ""
    loaned_printed_item = ""
    created_at = timezone.now()

    class Meta:
        model = LoanerModel




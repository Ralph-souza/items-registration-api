from django.db import models


class UserAuthModel(models.Model):
    auth_email = models.EmailField()
    user_password = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "User auth"

    def __str__(self) -> str:
        return self.auth_email

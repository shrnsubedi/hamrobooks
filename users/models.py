from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
  phone_regex = RegexValidator(
      regex=r"(?:\+977[- ])?\d{2}-?\d{7,8}",
      message="Incorrect Phone Number format! Phone number must be of format +977-01XXXXXX or +977-98XXXXXXXX",
  )
  phone = models.CharField(validators=[phone_regex], max_length=15, blank=False, null=False)
  address=models.CharField(max_length=50)

  def get_absolute_url(self):
      return reverse("login")
  



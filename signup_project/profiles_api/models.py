from django.db import models

# From django-phonenumber-field[phonenumberslite] pip package
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    name = models.CharField("real name", max_length=100)
    surname = models.CharField("last name", max_length=200)
    email = models.EmailField("e-mail address",max_length=200)
    phone = PhoneNumberField()
    validated_email = models.BooleanField("validated e-mail", default=False)
    validated_phone = models.BooleanField("validated phone number", default=False)
    def __str__(self):
        return "%s, %s" % (self.surname, self.name)
    def __repr__(self):
        return "%s, %s - %s, %s - %s, %s" % (self.surname, self.name, self.email, self.validated_email, self.phone, self.validated_phone)

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from profiles_api.models import Profile

admin.site.register(Profile)

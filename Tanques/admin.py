from django.contrib import admin
from .models import Tanques, config

# Register your models here.

admin.site.register(Tanques, config)

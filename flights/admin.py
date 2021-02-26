from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Airport)
admin.site.register(flight)
admin.site.register(Passenger)
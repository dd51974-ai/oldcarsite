from django.contrib import admin

# Register your models here.
from .models import Manufacturer
admin.site.register(Manufacturer)
from .models import Car
admin.site.register(Car)
from .models import Register
admin.site.register(Register)

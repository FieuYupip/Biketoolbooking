from django.contrib import admin
from .models import Toolbox, Building, Toolbox_rental

# Register your models here.
admin.site.register(Building),
admin.site.register(Toolbox),
admin.site.register(Toolbox_rental),
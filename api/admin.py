from django.contrib import admin
from .models import Station, Train, Stopover, Remark, Composition
# Register your models here.

admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Stopover)
admin.site.register(Remark)
admin.site.register(Composition)
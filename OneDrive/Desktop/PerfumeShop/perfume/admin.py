from django.contrib import admin
from .models import Perfume

class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Perfume, PerfumeAdmin)
  
from django.contrib import admin
from .models import FreeLancer


class FreeLancerAdmin(admin.ModelAdmin):
    list_display = ("user", "family", "father_name", "date_created")
    list_filter = ("done", "date_created")


admin.site.register(FreeLancer, FreeLancerAdmin)


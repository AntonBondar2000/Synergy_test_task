from django.contrib import admin

from apps.occupation.models import Occupation


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    pass

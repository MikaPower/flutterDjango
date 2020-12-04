from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Race
from .models import Pilot

admin.site.register(Pilot)


class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)
    fieldsets = (
        (1, {
            'fields': (
                'name', 'image'),
        }),
    )


admin.site.register(Race, RaceAdmin)

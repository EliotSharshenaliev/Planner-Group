from django.contrib import admin
from django.utils import timezone

from tours.models import Months, TourItem, Tourists


def duplicate_items(modeladmin, request, queryset):
    for obj in queryset:
        obj.pk = None
        obj.created_at = timezone.now()
        obj.save()

def update_spots(modeladmin, request, queryset):
    queryset.update(spots_total=25)


update_spots.short_description = "Установить количество для выбранных объектов"
duplicate_items.short_description = "Дублировать запись"

@admin.register(Months)
class MonthsAdmin(admin.ModelAdmin):
    actions = [duplicate_items]


@admin.register(TourItem)
class TourItemAdmin(admin.ModelAdmin):
    list_display = ("date_range", "months", "spots_total", "price", "created_at")
    actions = [duplicate_items, update_spots]


@admin.register(Tourists)
class TouristsAdmin(admin.ModelAdmin):
    pass
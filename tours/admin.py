from django.contrib import admin

from tours.models import Months, TourItem, Tourists


@admin.register(Months)
class MonthsAdmin(admin.ModelAdmin):
    pass


@admin.register(TourItem)
class TourItemAdmin(admin.ModelAdmin):
    list_display = ("months", "spots_total", "price", "spots_left", "created_at")


@admin.register(Tourists)
class TouristsAdmin(admin.ModelAdmin):
    pass
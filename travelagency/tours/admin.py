from django.contrib import admin
from .models import *


class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'time_update', 'time_create')
    list_display_links = ('title',)
    list_filter = ('time_update', 'cost', 'category')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'country')
    list_editable = ('rating',)
    list_filter = ('name', 'rating', 'country')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel_number')
    list_editable = ('tel_number',)
    list_filter = ('name', 'tel_number')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {"slugify_name": ('name',)}


class TicketAdmin(admin.ModelAdmin):
    list_display = ('tour', 'departure_date', 'term')
    list_filter = ('tour', 'term', 'departure_date')
    list_editable = ('term', 'departure_date')


class TermAdmin(admin.ModelAdmin):
    list_display = ('days',)
    list_filter = ('days',)


admin.site.register(Tour, TourAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Term, TermAdmin)

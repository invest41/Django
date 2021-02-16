from django.contrib import admin
from .models import Poll, Offer


class PollAdmin(admin.ModelAdmin):
 list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
 list_display = ('code', 'description')

# Register your models here.
admin.site.register(Poll, PollAdmin)
admin.site.register(Offer, OfferAdmin)

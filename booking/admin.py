from django.contrib import admin
from .models import Place, Adventure, User, Booking, Amenity, Itinerary, Review


class AdventureAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "slots", "image")

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number")

class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("name", "day", "image")
    list_filter = ("adventure_id",)

# Register your models here.
admin.site.register(Place)
admin.site.register(Adventure, AdventureAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Booking)
admin.site.register(Amenity)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(Review)

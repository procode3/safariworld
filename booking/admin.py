from django.contrib import admin
from .models import Place, Adventure, User, Booking, Amenity, Itinerary, Review

# Register your models here.
admin.site.register(Place)
admin.site.register(Adventure)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Amenity)
admin.site.register(Itinerary)
admin.site.register(Review)

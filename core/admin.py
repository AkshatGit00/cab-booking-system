from django.contrib import admin
from .models import Location, Rider, Cab, Trip

admin.site.register(Location)
admin.site.register(Rider)
admin.site.register(Cab)
admin.site.register(Trip)
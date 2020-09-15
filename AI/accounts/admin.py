from django.contrib import admin
from .models import User, Point, DateCount

admin.site.register(User)
admin.site.register(Point)
admin.site.register(DateCount)
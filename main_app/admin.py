from django.contrib import admin
from .models import Cheatsheet, Review, Favorite, Photo
# Register your models here.
admin.site.register(Cheatsheet)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Photo)

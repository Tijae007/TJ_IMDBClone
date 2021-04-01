from django.contrib import admin
from .models import Movie, MovieLinks

# Register your models here.
admin.site.site_header = 'TJ CINEMA DESIGN'
admin.site.register(Movie)
admin.site.register(MovieLinks)

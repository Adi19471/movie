from django.contrib import admin
from.models import *
# Register your models here.
@admin.register(Movie)

class Movie(admin.ModelAdmin):
    list_dispay = ('id','name',)
    list_display_links =  None
    
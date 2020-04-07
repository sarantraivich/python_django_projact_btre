from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published', 'address', 'city', 'state', 'photo_main')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'address', 'city', 'state')
    list_editable = ('is_published',)

admin.site.register(Listing, ListingAdmin)

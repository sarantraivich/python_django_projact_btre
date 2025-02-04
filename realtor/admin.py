from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'phone', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone', 'email')
    list_per_page = 25
    list_editable = ('is_mvp',)
    

admin.site.register(Realtor, RealtorAdmin)

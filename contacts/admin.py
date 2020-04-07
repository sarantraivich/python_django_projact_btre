from django.contrib import admin

from .models import contact

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'listing')

admin.site.register(contact, ContactsAdmin)

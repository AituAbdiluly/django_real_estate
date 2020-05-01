from django.contrib import admin

from .models import Contact

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('listing_id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact ,ContactsAdmin)
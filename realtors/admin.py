from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'hire_date', 'email')
    list_filter = ('hire_date',)

admin.site.register(Realtor, RealtorAdmin)

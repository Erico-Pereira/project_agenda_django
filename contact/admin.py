from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class Contact_admin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    ordering = 'id',
    # list_filter = 'created_ate',
    search_fields = 'first_name',
    list_per_page = 1
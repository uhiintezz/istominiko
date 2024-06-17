from django.contrib import admin

# Register your models here.
from .models import Contact



@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('name',)
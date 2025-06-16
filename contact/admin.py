from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at', 'updated_at')
    fields = ('name', 'email', 'message', 'notes', 'created_at', 'updated_at')
    
    def status_display(self, obj):
        if obj.is_replied:
            return format_html('<span style="color: green;">✓ Replied</span>')
        elif obj.is_read:
            return format_html('<span style="color: orange;">📖 Read</span>')
        else:
            return format_html('<span style="color: red;">✉️ New</span>')

    
    

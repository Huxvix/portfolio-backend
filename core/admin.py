from django.contrib import admin
from django.utils.html import format_html
from .models import PersonalInfo, Skill

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'location')
    search_fields = ('name', 'title', 'email', 'location')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'bio', 'profile_picture')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'github_url')
        }),
        ('Files', {
            'fields': ('resume_url',)
        }),
        ('Availability', {
            'fields': ('is_available_for_work', 'availability_message')
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_readonly_fields(self, request, obj=None):
        readonly = list(self.readonly_fields)
        if obj:  # Editing an existing object
            readonly.extend(['created_at', 'updated_at'])
        return readonly
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)

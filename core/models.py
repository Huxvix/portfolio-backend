from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', storage=MediaCloudinaryStorage(), blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    # Social links
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    
    # Files
    resume_file = models.FileField(upload_to='resume/', storage=MediaCloudinaryStorage(), blank=True, null=True)
    
    # Availability
    is_available_for_work = models.BooleanField(default=True)
    availability_message = models.CharField(
        max_length=200, 
        blank=True, 
        help_text="e.g., 'Available for freelance projects starting January 2024'"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Programming Language'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('software', 'Software'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.CharField(max_length=50, blank=True, help_text="React (FontAwesome) icon class, e.g. 'fab fa-react'")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']

from rest_framework import serializers
from .models import PersonalInfo, Skill

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = [
            'id', 'name', 'title', 'bio', 'profile_picture', 'email', 'phone', 'location',
            'linkedin_url', 'github_url', 'twitter_url', 'portfolio_url',
            'resume_file', 'is_available_for_work', 'availability_message',
            'created_at', 'updated_at'
        ]

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'icon', 'is_active', 'created_at', 'updated_at'] 
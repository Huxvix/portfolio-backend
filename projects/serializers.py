from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'image', 'url', 'github_url', 'technologies', 'created_at', 'updated_at'
        ]

    def get_technologies(self, obj):
        return [skill.name for skill in obj.skills.all()] 
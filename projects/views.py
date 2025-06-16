from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.filter(is_active=True)
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonalInfo, Skill
from .serializers import PersonalInfoSerializer, SkillSerializer

# Create your views here.

class PersonalInfoAPIView(APIView):
    def get(self, request):
        info = PersonalInfo.objects.first()
        if info:
            serializer = PersonalInfoSerializer(info, context={'request': request})
            return Response(serializer.data)
        return Response({'detail': 'Personal info not found.'}, status=status.HTTP_404_NOT_FOUND)

class SkillListAPIView(APIView):
    def get(self, request):
        skills = Skill.objects.filter(is_active=True)
        serializer = SkillSerializer(skills, many=True, context={'request': request})
        return Response(serializer.data)

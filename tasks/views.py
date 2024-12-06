from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Company_Project, User
from .serializers import UserSerializer, Company_ProjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

class Company_ProjectViewSet(viewsets.ModelViewSet):
    queryset = Company_Project.objects.all().order_by('-created_at')
    serializer_class = Company_ProjectSerializer

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'User created successfully',
        }, status=status.HTTP_201_CREATED)
    return Response({
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_project(request):
    serializer = Company_ProjectSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save()
        return Response({
            'message': 'Project created successfully',
        }, status=status.HTTP_201_CREATED)
    return Response({
        'message': 'Project not created',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_list(request):
    projects = Company_Project.objects.all()
    serializer = Company_ProjectSerializer(projects, many=True)
    return Response(serializer.data)
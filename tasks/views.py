from rest_framework import viewsets, status # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .models import Task, User
from .serializers import TaskSerializer, UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'User created successfully',
                
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'User not created',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

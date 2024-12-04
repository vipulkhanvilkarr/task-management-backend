from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from tasks.views import TaskViewSet, UserViewSet, create_user, user_list

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/create_user/', create_user, name='create_user'),
    path('api/user_list/', user_list, name='user_list'),
]
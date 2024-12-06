from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, Company_ProjectViewSet, create_user, user_list, create_project, project_list

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', Company_ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('create_user/', create_user, name='create_user'),
    path('user_list/', user_list, name='user_list'),
    path('comapny_project/create_project/', create_project, name='create_project'),
    path('comapny_project/project_list/', project_list, name='project_list'),
]
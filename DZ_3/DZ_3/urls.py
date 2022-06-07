from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import UserModelViewSet, ProjectModeViewSet, TodoModeViewSet


router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('project', ProjectModeViewSet)
router.register('todo', TodoModeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]

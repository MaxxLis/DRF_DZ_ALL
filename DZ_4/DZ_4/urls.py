from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userwork.views import UserModelViewSet, TodoModeViewSet, ProjectLimitOffsetPaginationViewSet

router = DefaultRouter()
filter_router = DefaultRouter()

router.register('users', UserModelViewSet)
router.register('project', ProjectLimitOffsetPaginationViewSet)
router.register('todo', TodoModeViewSet)
filter_router.register('param', ProjectLimitOffsetPaginationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('filters/', include(filter_router.urls)),
]

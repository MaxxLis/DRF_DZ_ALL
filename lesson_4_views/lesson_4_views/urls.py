from django.contrib import admin
from django.urls import path, include
from mainapp import views
from rest_framework.routers import DefaultRouter
from mainapp.views import ArticleCustomViewSet

router = DefaultRouter()
router.register('articles', ArticleCustomViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

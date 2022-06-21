from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'plants', views.PlantViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'metrics', views.MetricsViewSet)
router.register(r'sensorsBox', views.SensorBoxViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

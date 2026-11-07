from rest_framework.routers import DefaultRouter
from .api_views import ProductoViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet, basename='api-producto')



urlpatterns = router.urls


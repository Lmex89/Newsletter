from rest_framework.routers import DefaultRouter

from Categoria.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categoria/',CategoriaViewSet)

urlpatterns = router.urls
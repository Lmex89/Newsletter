
from rest_framework.routers import DefaultRouter

from Boletin.views import BoletinViewSet,VotacionesViewSet

router = DefaultRouter()
router.register(r'boletin',BoletinViewSet)
router.register(r'votacion',VotacionesViewSet)

urlpatterns = router.urls
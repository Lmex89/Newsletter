from rest_framework.routers import DefaultRouter

from Users.views import UserViewSet

router = DefaultRouter()
router.register(r'usuarios',UserViewSet)


urlpatterns = router.urls
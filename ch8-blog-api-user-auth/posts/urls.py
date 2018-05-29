from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('', views.PostViewSet)
router.register('users/', views.UserViewSet)
urlpatterns = router.urls

from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet

# urlpatterns = [
#     path('', views.PostList.as_view()),
#     path('<int:pk>/', views.PostDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]


router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MenuViewSet, RestaurantViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

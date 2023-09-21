from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CurrentDayMenuView, CurrentDayResultsView, EmployeeViewSet,
                    MenuViewSet, RestaurantViewSet, VoteViewSet)

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'current-day-menu', VoteViewSet)
router.register(r'current-day-results', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('current-day-menu/', CurrentDayMenuView.as_view(), name='current-day-menu'),
    path('current-day-results/', CurrentDayResultsView.as_view(), name='current-day-results')
]

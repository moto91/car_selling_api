from django.urls import path, include
from app import views
from rest_framework import routers

# Create a router and register ViewSet with it.
router = routers.DefaultRouter()
router.register(r'car_ads', views.CarAdViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]

urlpatterns += router.urls

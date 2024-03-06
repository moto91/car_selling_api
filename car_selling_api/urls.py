from django.urls import path, include
from app import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'car_ads', views.CarAdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls

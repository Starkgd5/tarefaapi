from django.urls import path, include
from rest_framework import routers
from core.views import UserViewSet, TaskViewSet, CepAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('address/<str:cep>/', CepAPIView.as_view(), name='address_from_cep')
]

urlpatterns += router.urls
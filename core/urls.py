from django.urls import include, path
from rest_framework import routers

from core.views import (CepAPIView, TaskViewSet, UserViewSet, user_create,
                        user_list)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('address/<str:cep>/', CepAPIView.as_view(), name='address_from_cep'),
    path('user_list/', user_list, name='user_list'),
    path('user_create/', user_create, name='user_create'),
]

urlpatterns += router.urls

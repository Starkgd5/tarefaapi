from django.urls import include, path
from rest_framework import routers

from core.views import (CepAPIView, TaskViewSet, UserViewSet, task_create,
                        task_list, user_create, user_delete, user_edit,
                        user_list)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('address/<str:cep>/', CepAPIView.as_view(), name='address_from_cep'),
    path('user_list/', user_list, name='user_list'),
    path('user_create/', user_create, name='user_create'),
    path('user_edit/<user_id>/', user_edit, name='user_edit'),
    path('user_delete/<user_id>/', user_delete, name='user_delete'),
    path('task_list/', task_list, name='task_list'),
    path('task_create/', task_create, name='task_create'),
]

urlpatterns += router.urls

import requests
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, response, status, viewsets

from core.models import Task
from core.serializers import CepSerializer, TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CepAPIView(generics.GenericAPIView):
    serializer_class = CepSerializer
    lookup_field = 'cep'

    def get_address_from_cep(self, cep):
        cep = cep.replace('-', '')
        url = f'https://viacep.com.br/ws/{cep}/json/'
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            return res.json()
        else:
            return None

    def get(self, request, **kwargs):
        cep = kwargs.get('cep')
        address_data = self.get_address_from_cep(cep)
        if not address_data:
            return response.Response({"message": "CEP not found"},
                                     status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(address_data)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


def user_list(request):
    return render(request, 'users/user_list.html')


def user_create(request):
    return render(request, 'users/user_create.html')


def user_edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, 'users/user_edit.html', context)


def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': user
    }
    return render(request, 'users/user_delete.html', context)


def task_list(request):
    return render(request, 'tasks/task_list.html')


def task_create(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'tasks/task_create.html', context)

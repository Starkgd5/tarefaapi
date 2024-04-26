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
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get(self, request, *args, **kwargs):
        cep = kwargs.get('cep')
        address_data = self.get_address_from_cep(cep)
        if address_data:
            serializer = self.get_serializer(address_data)
            return response.Response(serializer.data,
                                     status=status.HTTP_200_OK)
        else:
            return response.Response({"message": "CEP not found"},
                                     status=status.HTTP_400_BAD_REQUEST)


def user_list(request):
    return render(request, 'users/user_list.html')


def user_create(request):
    return render(request, 'users/user_create.html')

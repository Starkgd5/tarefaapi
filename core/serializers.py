from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Task


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'user']


class CepSerializer(serializers.Serializer):
    cep = serializers.CharField()
    logradouro = serializers.CharField()
    complemento = serializers.CharField()
    bairro = serializers.CharField()
    localidade = serializers.CharField()
    uf = serializers.CharField()
    ibge = serializers.CharField()
    gia = serializers.CharField()
    ddd = serializers.CharField()
    siafi = serializers.CharField()

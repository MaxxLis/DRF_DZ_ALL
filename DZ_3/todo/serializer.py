from rest_framework import serializers
from .models import Project, Todo
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # fields = ('username', 'id')
        fields = ['username']


class ProjectSerializer(serializers.ModelSerializer):
    users_project = serializers.StringRelatedField(many=True)

    # users_project = UserSerializer()

    class Meta:
        model = Project
        exclude = ['id']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    todo_user = UserSerializer()
    todo_project = ProjectSerializer()

    class Meta:
        model = Todo
        # exclude = ['id']
        fields = '__all__'

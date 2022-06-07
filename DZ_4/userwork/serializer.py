from rest_framework import serializers
from .models import Project, Todo
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProjectSerializer(serializers.ModelSerializer):
    users_project = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        exclude = ['id']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    todo_user = UserSerializer()
    todo_project = ProjectSerializer()

    class Meta:
        model = Todo
        fields = '__all__'
        # exclude = ['todo_project']

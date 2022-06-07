from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.generics import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer, ProjectSerializer, TodoSerializer
from .models import Project, Todo, User
from rest_framework.pagination import LimitOffsetPagination


class UserModelViewSet(
    # mixins.CreateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectLimitOffsetPaginationViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()
        if name:
            projects = projects.filter(name_project__contains=name)

        return projects


class TodoModeViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ['todo_project']

    def destroy(self, request, pk=None):
        queryset = get_object_or_404(Todo, pk=pk)
        queryset.todo_open_close = True
        queryset.save()
        response = {'message': 'Удалять сегодня не будем, просто пометим что закрыта...'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)




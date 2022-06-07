from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Article
from rest_framework.response import Response
from .serializer import ArticleSerializer

from rest_framework.generics import CreateAPIView, get_object_or_404


class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                           mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer
        renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

        # def get_queryset(self):
        #     return Article.objects.filter(name__contains="3")

# APIView
# class ArticleAPIVIew(APIView):
#     renderer_classes = [JSONRenderer]
#
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)


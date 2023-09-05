from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Post
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from ..serializers import PostSerializer, PostUpdateSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated]
  filterset_fields = ['user']
  search_fields = ['title', 'user']
  ordering_fields = ['title', 'date']

  def get_serializer_class(self):

    if self.action == 'create':
        return PostCreateSerializer
    elif self.action == 'update' or self.action == 'partial_update':
        return PostUpdateSerializer
    return PostSerializer

  def update(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.user == self.request.user:
          serializer = PostUpdateSerializer(instance, data=request.data, partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)
      return Response("You haven't permission to edit", status=status.HTTP_403_FORBIDDEN)

  def destroy(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.user == self.request.user:
          instance.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      return Response("You haven't permission to delete", status=status.HTTP_403_FORBIDDEN)

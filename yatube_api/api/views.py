from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from posts.models import Follow, Group, Post

from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """Получаем список всех публикаций.
    Работает с пагинацией.
    Позволяет только автору удалять/редактировать свои записи.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Показываем список групп, с пагинацией.
    Работает с пагинацией.
    Работает только на чтение.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LimitOffsetPagination


class CommentViewSet(viewsets.ModelViewSet):
    """Получаем и показываем комментарии.
    Позволяет только автору удалять/редактировать свои записи.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    """Получаем и показываем, на кого подписались.
    Доступно только для авторизованного пользователя.
    """
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def get_queryset(self):
        follow = Follow.objects.filter(user=self.request.user)
        return follow

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

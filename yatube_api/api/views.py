from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post

from .mixins import CreateListViewSet
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """Получаем список всех публикаций.
    Работает с пагинацией.
    Позволяет только автору удалять/редактировать свои записи.
    """
    queryset = Post.objects.select_related("group", "author")
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnlyPermission,)

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
    permission_classes = (IsAuthorOrReadOnlyPermission,)


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


class FollowViewSet(CreateListViewSet):
    """Получаем и показываем, на кого подписались.
    Доступно только для авторизованного пользователя.
    """
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

from django.shortcuts import get_object_or_404, redirect
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .models import Comment, Post, Tag
from .serializers import CommentSerializer, PostSerializer, TagSerializer
from .utils import IsAllowedToChangePost, IsAllowedToCreatePost


def temp_homepage(request):
    return redirect('main-api-page')


@api_view(['GET', ])
def main_api_page(request):
    posts_route = reverse('post-list-api', request=request)
    tags_route = reverse('tag-list-api', request=request)
    available_routes = [
        {'List of all the posts': posts_route},
        {'List of all the tags': tags_route},
    ]
    return Response(available_routes)


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [IsAllowedToCreatePost]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAllowedToChangePost]
    lookup_field = 'slug'


class CommentListAPI(generics.ListCreateAPIView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        return Comment.objects.filter(post=post)

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        serializer.save(author=self.request.user, post=post)


class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        post = get_object_or_404(Post, slug=slug)
        return Comment.objects.filter(post=post)

    serializer_class = CommentSerializer
    permission_classes = [IsAllowedToChangePost]


class TagListAPI(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAllowedToCreatePost]


class TagDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAllowedToCreatePost]

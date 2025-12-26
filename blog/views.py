from django.forms import model_to_dict
from django.shortcuts import render
from django.template.context_processors import request
from django.template.defaultfilters import title
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Blog, Category
from .permisions import IsAdminOrReadOnly
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = (IsAdminOrReadOnly, )


    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Blog.objects.all()

        return Blog.objects.filter(pk=pk)

    @action(methods=['get'],detail=True)
    def category(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
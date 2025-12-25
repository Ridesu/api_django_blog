from django.forms import model_to_dict
from django.shortcuts import render
from django.template.context_processors import request
from django.template.defaultfilters import title
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog
from .serializers import BlogSerializer

class BlogAPIView(APIView):
    def get(self, request):
        lst = Blog.objects.all().values()
        return Response(list(lst))

    def post(self, request):
        serial = BlogSerializer(data=request.data)
        serial.is_valid(raise_exception=True)

        post_new = Blog.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
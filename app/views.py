from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
# Create your views here.

# class PostView(APIView):
#     def get(self, request):
#         data = Post.objects.all()
#         seri = PostSerializer(data, many=True)
#         return Response(seri.data)
#     def post(self, request):
#         data = request.data
#         seri = PostSerializer(data=data)
#         if seri.is_valid():
#             seri.save()
#             return Response({"message": "Data is received"})
#         return Response({"message": "wrong"})
class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
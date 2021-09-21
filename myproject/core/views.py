from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .serializers import PostSerializer
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
  '''
  Este viewset fornece automaticamente ações em 'list' e 'detail'.
  '''
  queryset = User.objects.all()
  serializer_class = UserSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#   queryset = Comment.objects.all()
#   serializers_class = CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  

def upload_file(request):
  if request.method == 'POST':
        form = Post(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
  else:
    form = Post()
  return render(request, 'upload.html', {'form': form})
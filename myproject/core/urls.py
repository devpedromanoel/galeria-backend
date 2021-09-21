from django.urls import include, path
from django.urls.resolvers import URLPattern
from rest_framework import routers
from myproject.core import views as v


app_name = 'core'


router = routers.DefaultRouter()
router.register('user', v.UserViewSet)
router.register('posts', v.PostViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
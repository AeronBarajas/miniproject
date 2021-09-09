from django.urls import path, include
from rest_framework import routers
from mini.views import MiniViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'mini', MiniViewSet) #register '/blogs' routes

urlpatterns = [
     # add all of our router urls
    path('', include(router.urls)),
]

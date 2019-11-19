from django.urls import path, include
from . import views
from rest_framework import routers
import items.urls 
from items.views import ItemViewSet,CategoryViewSet,FavouriteViewSet
import items.models
from django.conf import settings
from django.conf.urls.static import static 

router = routers.DefaultRouter()




urlpatterns = [
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
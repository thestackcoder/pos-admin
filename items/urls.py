from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static 

router = routers.DefaultRouter()
# router.register('items', views.ItemViewSet)
# router.register('categories', views.CategoryViewSet)
# router.register('favourite', views.FavouriteViewSet)

urlpatterns = [
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include
from rest_framework import routers
import items.urls 
import orders.urls 
from items.views import ItemViewSet,CategoryViewSet,FavouriteViewSet,FavouriteItemViewSet
from orders.views import Order_itemViewSet,OrderViewSet,Order_detailViewSet
from actors.views import UserViewSet,CustomerViewSet, login
import actors.urls
from rest_framework_extensions.routers import ExtendedSimpleRouter
from django.conf import settings
from django.conf.urls.static import static 

category_item_router = ExtendedSimpleRouter()
(
    category_item_router.register(r'categories', UserViewSet, base_name='categories')
          .register(r'items',
                    ItemViewSet,
                    'categories_item',
                    parents_query_lookups=['category'])
)
user_favourite_router = ExtendedSimpleRouter()
(
    user_favourite_router.register(r'users', UserViewSet, base_name='users')
          .register(r'favourite',
                    FavouriteViewSet,
                    'users_favourite',
                    parents_query_lookups=['user'])
)
favourite_item_router = ExtendedSimpleRouter()
(
    favourite_item_router.register(r'users', UserViewSet, base_name='users')
          .register(r'favouriteitems',
                    FavouriteItemViewSet,
                    'users_favourite',
                    parents_query_lookups=['user'])
)
user_orders_router = ExtendedSimpleRouter()
(
    user_orders_router.register(r'users', UserViewSet, base_name='users')
          .register(r'orders',
                    OrderViewSet,
                    'users_orders',
                    parents_query_lookups=['user_id'])
)



router = routers.DefaultRouter()
router.register('users', actors.views.UserViewSet,base_name='users')
router.register('customers', CustomerViewSet,base_name='customers')
router.register('items', items.views.ItemViewSet)
router.register('categories',items.views.CategoryViewSet)
router.register('favourite', items.views.FavouriteViewSet,base_name='favourite')
router.register('favouriteitems', items.views.FavouriteItemViewSet,base_name='favouriteitems')
router.register('orders', orders.views.OrderViewSet)
# router.register('order_items', orders.views.Order_itemViewSet)
# router.register('orders_details', orders.views.Order_detailViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', include(category_item_router.urls)),  
    path('', include(user_favourite_router.urls)),
    path('', include(favourite_item_router.urls)), 
    path('', include(user_orders_router.urls)),
    path('login/', login, name="login"),
    # path('addfav/', addfav, name="addfav"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
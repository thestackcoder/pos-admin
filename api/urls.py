from django.urls import path, include
from rest_framework import routers
import items.urls 
import orders.urls 
from items.views import ItemViewSet,CategoryViewSet,FavouriteViewSet,FavouriteItemViewSet
from orders.views import Order_itemViewSet,OrderViewSet,Order_detailViewSet,updateStock,PosSystems
# TodoViewSet
from actors.views import UserViewSet,CustomerViewSet, login
import actors.urls
from rest_framework_extensions.routers import ExtendedSimpleRouter
from django.conf import settings
from django.conf.urls.static import static 



category_item_router = ExtendedSimpleRouter()
(
    category_item_router.register(r'categories', UserViewSet, basename='categories')
          .register(r'items',
                    ItemViewSet,
                    'categories_item',
                    parents_query_lookups=['category'])
)
user_favourite_router = ExtendedSimpleRouter()
(
    user_favourite_router.register(r'users', UserViewSet, basename='users')
          .register(r'favourite',
                    FavouriteViewSet,
                    'users_favourite',
                    parents_query_lookups=['user'])
)
favourite_item_router = ExtendedSimpleRouter()
(
    favourite_item_router.register(r'users', UserViewSet, basename='users')
          .register(r'favouriteitems',
                    FavouriteItemViewSet,
                    'users_favourite',
                    parents_query_lookups=['user'])
)
user_orders_router = ExtendedSimpleRouter()
(
    user_orders_router.register(r'users', UserViewSet, basename='users')
          .register(r'orders',
                    OrderViewSet,
                    'users_orders',
                    parents_query_lookups=['user_id'])
)



router = routers.DefaultRouter()
router.register('users', actors.views.UserViewSet,basename='users')
router.register('customers', CustomerViewSet,basename='customers')
router.register('items', items.views.ItemViewSet)
router.register('categories',items.views.CategoryViewSet)
# router.register('favourite', items.views.FavouriteViewSet,basename='favourite')
router.register('favouriteitems', items.views.FavouriteItemViewSet,basename='favouriteitems')
router.register('orders', orders.views.OrderViewSet, basename='orders')
router.register('petty-cash', PosSystems, basename='petty-cash')
# router.register('todo', TodoViewSet, basename='todo')

# router.register('order_items', orders.views.Order_itemViewSet)
# router.register('orders_details', orders.views.Order_detailViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', include(category_item_router.urls)),  
    path('', include(user_favourite_router.urls)),
    path('', include(favourite_item_router.urls)), 
    path('', include(user_orders_router.urls)),
    path('login/', login, name="login"),
    path('updateStock/', updateStock, name="updateStock"),
    # path('addfav/', addfav, name="addfav"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from rest_framework import serializers
from items.models import Category,Item,Favourite
from actors.models import User


class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category.name', required=False)
    image = serializers.ImageField(use_url=False)
    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'image', 'category', 'category_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]
        
class FavouriteSerializer(serializers.ModelSerializer):
    # user_name = serializers.StringRelatedField(source='user.username', required=False)
    # item_name = serializers.StringRelatedField(source='item.name', required=False)


    class Meta:
        model = Favourite
        fields = ['id', 'user', 'item']


class FavouriteItemSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    user_name = serializers.StringRelatedField(source='user.username', required=False)
    item_id = serializers.IntegerField(source='item.id', required=False)
    item_name = serializers.StringRelatedField(source='item.name', required=False)
    item_price = serializers.StringRelatedField(source='item.price', required=False)
    item_image = serializers.ImageField(source="item.image", use_url=False, required=False)
    item_category = serializers.StringRelatedField(source='item.category', required=False)
    class Meta:
        model = Favourite
        fields = ['id','user_id', 'user_name', 'item_id','item_name','item_price', 'item_image', 'item_category']


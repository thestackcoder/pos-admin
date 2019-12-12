from rest_framework import serializers
from actors.models import Customer,User
from items.models import Item,Favourite
from items.serializers import FavouriteSerializer
from rest_framework.serializers import HyperlinkedIdentityField,ModelSerializer,SerializerMethodField,ValidationError,CharField

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'RF_id','balance']
        
class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False,required=False)
    class Meta:
        model = User
        fields = ['id', 'name', 'username','password','contact', 'image']
        extra_kwargs = {"password":{"write_only":True}}

    # def get_image(self, user):
    #     request = self.context.get('request')
    #     image = user.image.url
    #     return request.get_full_path(image)
        
        


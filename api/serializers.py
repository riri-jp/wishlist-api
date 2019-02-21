from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',            
        ]
class FavoriteItemSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = FavoriteItem
        fields = [
            'user',
        ]
class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField( 
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id",
    )
    added_by = UserSerializer()
    user_count_fav = serializers.SerializerMethodField()
     
    class Meta:
        model = Item
        fields = [
            'name',
            'image',
            'description',
            'detail',
            'added_by',
            'user_count_fav',
            ]
    def  get_user_count_fav(self, obj):
        return obj.users.count()


class ItemDetailSerializer(serializers.ModelSerializer):
    users = FavoriteItemSerializer(many=True)
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'image',
            'description',
            'users',
            ]
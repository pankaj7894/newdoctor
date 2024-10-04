from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'mobile', 'usertype','password','is_verified','is_active','is_verified']
        extra_kwargs = {'password': {'write_only': True}, 'is_verified': {'read_only': True}, 'is_active': {'read_only': True}}

    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            mobile=validated_data['mobile'],
            usertype=validated_data['usertype'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

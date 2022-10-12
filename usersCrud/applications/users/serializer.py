from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser
from .models import Users
from utils import update_attrs

class DjangoUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DjangoUser
        fields = "__all__"

class RelatedDjangoUser(serializers.RelatedField):

    def __init__(self, **kwargs):
        self.action = None
        super().__init__(**kwargs)

    def to_representation(self, value):
        return DjangoUserSerializer(value).data
    
    def to_internal_value(self, data):
        return data

class UserSerializer(serializers.ModelSerializer):

    DjangoUser = RelatedDjangoUser(required=True,queryset=DjangoUser.objects.all())
    UUID = serializers.UUIDField(required=False)

    class Meta:
        model = Users
        fields = "__all__"
    
    def create(self, validated_data):
        validated_data["DjangoUser"] = DjangoUserSerializer().create(validated_data["DjangoUser"])
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data["DjangoUser"] = DjangoUserSerializer().update(instance.DjangoUser,validated_data["DjangoUser"])
        return update_attrs(instance, **validated_data)
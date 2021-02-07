from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Account, Customer, Transfer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        exclude = []


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        exclude = []


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        exclude = []


"""
class AccountSerializer(serializers.Serializer):

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance
    
    """
from rest_framework.serializers import ModelSerializer
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

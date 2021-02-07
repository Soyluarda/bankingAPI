from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Account, Customer, Transfer
from .serializers import AccountSerializer, CustomerSerializer, TransferSerializer
from rest_framework.generics import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse


class AccountList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        return Response({'customer': customer})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountView(APIView):
    def get(self, request, pk=None):
        if pk:
            article = get_object_or_404(Account.objects.all(), pk=pk)
            serializer = AccountSerializer(article)
            return Response({"account": serializer.data})
        articles = Account.objects.all()
        serializer = AccountSerializer(articles, many=True)
        return Response({"accounts": serializer.data})

    def post(self, request):
        data = request.data
        serializer = AccountSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            saved_account = serializer.save()
        return Response({"success": "Account for '{}' created successfully".format(saved_account)})


class TransferView(APIView):
    def post(self, request):
        data = request.data
        serializer = TransferSerializer(data=data)
        transfer_from_account = request.data.get('from_account')
        transfer_amount = int(request.data.get('amount'))
        from_account = Account.objects.get(id=transfer_from_account)
        if transfer_amount > from_account.amount:
            return Response({"wrong": "Account amount is not enough for this transfer."})

        if serializer.is_valid(raise_exception=True):
            saved_transfer = serializer.save()
            saved_transfer._transfer_amount()
            return Response({"success": "{} amount Transfer from {} to {} successfully".format(saved_transfer.amount, saved_transfer.from_account, saved_transfer.to_account)})

    def get(self, request, pk=None):
        if pk:
            data = list(Transfer.objects.filter(Q(from_account=pk) | Q(to_account=pk)).values().order_by('-date'))
            return JsonResponse({'transfers': data})

        transfers = Transfer.objects.all()
        serializer = TransferSerializer(transfers, many=True)
        return Response({"transfer": serializer.data})

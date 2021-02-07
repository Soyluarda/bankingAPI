from django.test import TestCase
from main.models import Account, Customer, Transfer


class TransferTests(TestCase):

    def setUp(self):
        super(TransferTests, self).setUp()

        self.customer = Customer.objects.create(name="Arisha Barron")
        self.amount = 100
        self.customer2 = Customer.objects.create(name="Branden Gibson")

    def test_create_transfer(self):
        account = Account.objects.create(customer=self.customer, amount=self.amount)
        account2 = Account.objects.create(customer=self.customer2, amount=self.amount)

        transfer = Transfer.objects.create(from_account=account, to_account=account2, amount=self.amount)
        result = {
            'from_account': transfer.from_account.customer.name,
            'to_account': transfer.to_account.customer.name,
            'amount': transfer.amount
        }

        self.assertEqual(result, {'from_account': "Arisha Barron", "to_account": "Branden Gibson", 'amount': 100})

    def test_transfer(self):
        account = Account.objects.create(customer=self.customer, amount=self.amount)
        account2 = Account.objects.create(customer=self.customer2, amount=self.amount)

        transfer = Transfer.objects.create(from_account=account, to_account=account2, amount=self.amount)
        transfer._transfer_amount()

        result = {
            transfer.from_account.customer.name: transfer.from_account.amount,
            transfer.to_account.customer.name: transfer.to_account.amount,
        }

        self.assertEqual(result, {'Arisha Barron': 0, 'Branden Gibson': 200})

from django.test import TestCase
from main.models import Account, Customer, Transfer


class AccountTests(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="Arisha Barron")
        self.amount = 100
        self.customer2 = Customer.objects.create(name="Branden Gibson")

    def test_create_account(self):
        account = Account.objects.create(customer=self.customer, amount=100)

        result = {
            'name': account.customer.name,
            'amount': account.amount
        }

        self.assertEqual(result, {'name': "Arisha Barron", 'amount': 100})

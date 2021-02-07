from django.test import TestCase
from main.models import Account, Customer, Transfer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class APITests(TestCase):

    def setUp(self):
        super(APITests, self).setUp()
        self.customer = Customer.objects.create(name="Arisha Barron")
        self.amount = 100
        self.customer2 = Customer.objects.create(name="Branden Gibson")

        user = User.objects.create(username='username')
        user.set_password('password')
        user.save()
        self.user = user
        self.token = Token.objects.create(user=user)

    def test_account_api(self):
        Account.objects.create(customer=self.customer, amount=self.amount)
        url = '/accounts/1/'
        data = {'username': "username", 'password': 'password'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.data['account'], {'id': 1, 'amount': 100, 'customer': 1})

    def test_accounts_api(self):
        Account.objects.create(customer=self.customer, amount=self.amount)
        url = '/accounts/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['account'], {'id': 1, 'amount': 100, 'customer': 1})

    def test_customers_api(self):
        Customer.objects.create(name="Dopigo")
        url = '/customers/3/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, {'id': 3, 'name': 'Dopigo'})

        url = '/customers/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, [{'id': 1, 'name': 'Arisha Barron'},{'id': 2, 'name': 'Branden Gibson'},{'id': 3, 'name': 'Dopigo'}])

    def test_transfer_api(self):
        account = Account.objects.create(customer=self.customer, amount=self.amount)
        account2 = Account.objects.create(customer=self.customer2, amount=self.amount)

        transfer = Transfer.objects.create(from_account=account, to_account=account2, amount=self.amount)
        transfer._transfer_amount()

        url = '/transfer/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.json()['transfer'][0]['id'], 1)
        self.assertEqual(response.json()['transfer'][0]['amount'], 100)

        url = '/accounts/' + str(account.id) + '/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['account'], {'id': 1, 'amount': 0, 'customer': 1})

        url = '/accounts/' + str(account2.id) + '/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['account'], {'id': 2, 'amount': 200, 'customer': 2})
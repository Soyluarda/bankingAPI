from django.db import models
from django.db import transaction


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.customer.name


class Transfer(models.Model):
    from_account = models.ForeignKey(Account, related_name='from_account', on_delete=models.CASCADE)
    to_account = models.ForeignKey(Account, related_name='to_account', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def _transfer_amount(self):
        with transaction.atomic():
            self.from_account.amount -= self.amount
            self.to_account.amount += self.amount

            self.from_account.save()
            self.to_account.save()

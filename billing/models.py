from django.db import models
from django.contrib.auth import get_user_model

from book_mgt.models import BookLoan


class Fine(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(BookLoan, on_delete=models.CASCADE)
    amount_per_day = models.FloatField(default=2.0)
    total_amount = models.FloatField()
    amount_paid = models.FloatField()
    balance = models.FloatField()

    def __str__(self):
        return f'{self.user} - {self.total_amount} (balance = {self.balance})'

    @property
    def total_amount(self):
        return self.book.days_overdue * self.amount_per_day

    @property
    def balance(self):
        return self.total_amount - self.amount_paid

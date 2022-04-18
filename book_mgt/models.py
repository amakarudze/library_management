from datetime import date, timedelta

from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Author(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    code = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=6)
    edition = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def checkout_book(self):
        self.available = False
        self.save(update_fields=["available"])

    def return_book(self):
        self.available = True
        self.save(update_fields=["available"])


class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    date_loaned_out = models.DateField(auto_now_add=True)
    date_due = models.DateField()
    returned = models.BooleanField(default=False)
    date_returned = models.DateField(blank=True, null=True)
    is_overdue = models.BooleanField(default=False)
    days_overdue = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user} - {self.book}"

    @property
    def date_due(self):
        return self.date_loaned_out + timedelta(days=7)

    @property
    def is_overdue(self):
        today = date.today()
        return bool(today > self.date_due)

    @property
    def days_overdue(self):
        if self.is_overdue and self.date_returned:
            days_overdue = self.date_returned.date() - self.date_due.date()
            return days_overdue.days
        elif self.is_overdue and not self.date_returned:
            days_overdue = date.today() - self.date_due.date()
            return days_overdue.days
        else:
            return 0

    def overdue_email_notification(self):
        template = 'emails/overdue_email.html'
        subject = f'The {self.book} you borrowed is overdue.'
        message = render_to_string(template, {})
        from_email = ''
        to_email = self.user.email
        send_mail(subject, message, from_email, [to_email], html_message=message)

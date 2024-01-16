# models.py

from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Transactions(models.Model):
    CATEGORY_CHOICES = [
        ('income', 'Дохід'),
        ('expense', 'Витрата'),
    ]

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.transaction_type} - {self.sum}"

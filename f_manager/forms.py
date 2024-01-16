# forms.py

from django import forms
from .models import Transactions, Categories

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['category', 'transaction_type', 'sum', 'date', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description']
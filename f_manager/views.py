from django.shortcuts import render, redirect, get_object_or_404
from .models import Transactions, Categories
from .forms import TransactionForm, CategoryForm

def list_of_categories(request):
    categories = Categories.objects.all()
    return render(request, 'list-of-categories.html', {'categories': categories})

def add_categories(request, category_id=None):
    if category_id is not None:
        category = get_object_or_404(Categories, id=category_id)
    else:
        category = Categories()

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('list-of-categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'add-categories.html', {'form': form})


def delete_categories(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    
    if request.method == 'POST':
        category.delete()
        return redirect('list-of-categories')

    return render(request, 'delete-categories.html', {'category': category})

def list_of_transactions(request):
    transactions = Transactions.objects.all()
    return render(request, 'list-of-transactions.html', {'transactions': transactions})

def add_transactions(request, transaction_id=None):
    if transaction_id is not None:
        transaction = get_object_or_404(Transactions, id=transaction_id)
    else:
        transaction = Transactions()

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
            return redirect('list-of-transactions')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'add-transactions.html', {'form': form, 'categories': Categories.objects.all()})

def delete_transactions(request, transaction_id):
    transaction = get_object_or_404(Transactions, id=transaction_id)
    
    if request.method == 'POST':
        transaction.delete()
        return redirect('list-of-transactions')

    return render(request, 'delete-transactions.html', {'transaction': transaction})

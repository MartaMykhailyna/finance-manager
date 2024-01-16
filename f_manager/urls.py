# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add-categories/', views.add_categories, name='add-categories'),
    path('edit-categories/<int:category_id>/', views.add_categories, name='edit-categories'),
    path('delete-categories/<int:category_id>/', views.delete_categories, name='delete-categories'),
    path('list-of-categories/', views.list_of_categories, name='list-of-categories'),
    path('add-transactions/', views.add_transactions, name='add-transactions'),
    path('edit-transactions/<int:transaction_id>/', views.add_transactions, name='edit-transactions'),
    path('delete-transactions/<int:transaction_id>/', views.delete_transactions, name='delete-transactions'),
    path('list-of-transactions/', views.list_of_transactions, name='list-of-transactions'),
]

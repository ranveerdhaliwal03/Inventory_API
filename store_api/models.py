"""
    File: models.py
    Author: [Ranveer Dhaliwal]
    Date: [2023-08-18]
"""

# Import necessary modules and classes
from django.db import models

class Item(models.Model):
    """
    Represents an item in the inventory.

    Attributes:
        name (str): The name of the item (up to 100 characters).
        item_number (int): The item number.
        price (Decimal): The price of the item with up to 10 digits and 2 decimal places.
        quantity (int): The quantity of the item available.
        date_acquired (Date): The date when the item was acquired.

    Methods:
        __str__(): Returns the name of the item as its string representation.


    """
    name = models.CharField(max_length=100)
    item_number = models.IntegerField(max_length=20)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_acquired = models.DateField()


    def __str__(self):
        return self.name
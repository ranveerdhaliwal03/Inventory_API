"""
    File: serializer.py
    Author: [Ranveer Dhaliwal]
    Date: [2023-08-18]
"""

# Import necessary modules and classes
from rest_framework import serializers
from store_api.models import Item
from django.forms import ValidationError
from django.utils import timezone



class ItemSerializer(serializers.ModelSerializer):
    """
    Attributes:
        description (str): Field to provide a description of the item.

    Methods:
        get_description(data): Returns a description of the item using its name and quantity.
        validate_name(value): Validates whether an item with the given name already exists.
        validate_item_number(value): Validates whether an item with the given item number already exists.
        validate_quantity(value): Validates that the quantity is not over 5000.
        validate_date_acquired(value): Validates that the date acquired is not in the future.
    """
    

    description = serializers.SerializerMethodField()
   
    class Meta: 
        model = Item
        fields = "__all__"

    #creates a description for the item, displaying the item's name and quantity
    def get_description(self, data):   
        """
        Returns a description of the item.

        Args:
            data (Item): The item instance.

        Returns:
            str: A description of the item including its name and quantity.
        """
        return "This Item is called " + data.name + " and there is " + str(data.quantity) + " avaliable."
    
    #Check if an item with the given name already exists
    def validate_name(self, value): 
        """
        Validates whether an item with the given name already exists.

        Args:
            value (str): The name of the item to be validated.

        Returns:
            str: The validated item name.

        Raises:
            ValidationError: If an item with the same name already exists.
        """
        existing_item = Item.objects.filter(name=value).first() 

        if existing_item:
            raise ValidationError("An item with this name already exists.")
        return value
    
     # Check if an item with the given item number already exists:
    def validate_item_number(self, value):
        """
        Validates whether an item with the given item number already exists.

        Args:
            value (int): The item number to be validated.

        Returns:
            int: The validated item number.

        Raises:
            ValidationError: If an item with the same item number already exists.
        """
        existing_item = Item.objects.filter(name=value).first() 
        if existing_item:
            raise ValidationError("An item with this item number already exists.")
        return value
    
    # Check if quantity is not over 5000
    def validate_quantity(self, value):   
        """
        Validates that the quantity is not over 5000.

        Args:
            value (int): The quantity of the item to be validated.

        Returns:
            int: The validated quantity.

        Raises:
            ValidationError: If the quantity is over 5000.
        """
        if value > 5000:
            raise ValidationError("Quantity cannot be over 5000.")
        return value
    
    # Check if date is not in the future
    def validate_date_acquired(self, value):  
        """
        Validates that the date acquired is not in the future.

        Args:
            value (Date): The date acquired to be validated.

        Returns:
            Date: The validated date acquired.

        Raises:
            ValidationError: If the date is in the future.
        """
        if value > timezone.now().date():
            raise ValidationError("Date cannot be in the future.")
        return value


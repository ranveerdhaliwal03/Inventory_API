"""
    File: views.py
    Author: [Ranveer Dhaliwal]
    Date: [2023-08-18]
"""

# Import necessary modules and classes
from django.shortcuts import render
from store_api.models import Item
from store_api.serializer import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 


class ItemList(APIView):  # GET: List all items
    """
    View for listing all items or creating a new item.

    Attributes:
        None

    Methods:
        get(request): Handles GET request to list all items.
    """

    def get(self, request):                             #END POINT 1 TO GET BOOKS  /BOOKS/LIST
        """
        Handle GET request to list all items.

        Args:
            request (Request): The GET request.

        Returns:
            Response: JSON response containing a list of all items.
        """
        items = Item.objects.all()                      #complex data, not py code, need to convert it to py dic & list
        serializer = ItemSerializer(items, many=True)   #returned value will be json
        return Response(serializer.data)
    


class ItemCreate(APIView):  # POST: Create new item
    """
    View for creating a new item.

    Attributes:
        None

    Methods:
        post(request): Handles POST request to create a new item.
    """
    def post(self, request):
        """
        Handle POST request to create a new item.

        Args:
            request (Request): The POST request with item data.

        Returns:
            Response: JSON response with the created item data or errors if validation fails.
        """

        serializer = ItemSerializer(data=request.data) # data=request.data ---- it knows to convert from json-> cmplx data
        if serializer.is_valid(): #make sure the data 'posting' is valid
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #change status to not show 200 (make it 400 meaning smthing wrong)
        

class ItemDetail(APIView): # GET, PUT, DELETE: Item details       UPDATE/DELETE
    """
    View for retrieving, updating, or deleting an item.

    Attributes:
        None

    Methods:
        get_item_pk(pk): Get the item by primary key or return a 404 error if not found.
        get(request, pk): Handles GET request to retrieve an item.
        put(request, pk): Handles PUT request to update an item.
        delete(request, pk): Handles DELETE request to delete an item.
    """
    def get_item_pk(self, pk): #gets the primary key of the item
        """
        Get the item by primary key or return a 404 error if not found.

        Args:
            pk (int): The primary key of the item.

        Returns:
            Item: The item with the specified primary key.
            Response: A 404 error response if the item is not found.
        """
        try:
            return Item.objects.get(pk=pk)
        except:
            return Response({ "ERROR": "Book does not exist"}, status=status.HTTP_404_NOT_FOUND)  #if item DNE
        

    def get(self, request, pk):
        """
        Handle GET request to retrieve an item.

        Args:
            request (Request): The GET request.
            pk (int): The primary key of the item.

        Returns:
            Response: JSON response containing the retrieved item data or a 404 error if not found.
        """
        items = self.get_item_pk(pk)                    #complex data, not py code, need to convert it to py dic & list
        serializer = ItemSerializer(items)              #returned value will be json
        return Response(serializer.data)


    def put(self, request, pk):
        """
        Handle PUT request to update an item.

        Args:
            request (Request): The PUT request with updated item data.
            pk (int): The primary key of the item.

        Returns:
            Response: JSON response with the updated item data or errors if validation fails.
        """
        item= self.get_item_pk(pk)                    #complex data, not py code, need to convert it to py dic & list
        serializer = ItemSerializer(item, data=request.data) #passing the instance that we want to update aswell as the updated value
        if serializer.is_valid():   #make sure the data 'posting' is valid
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #change status to not show 200 (make it 400 meaning smthing wrong)
    
    def delete(self,request, pk):
        """
        Handle DELETE request to delete an item.

        Args:
            request (Request): The DELETE request.
            pk (int): The primary key of the item.

        Returns:
            Response: A 204 No Content response indicating successful item deletion.
        """
        item = self.get_item_pk(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
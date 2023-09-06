
from django.contrib import admin
from django.urls import path, include
from store_api.views import ItemList, ItemCreate, ItemDetail

urlpatterns = [
    path('', ItemCreate.as_view()),      # POST: Create new item
    path('list/', ItemList.as_view()),   # GET: List all items
    path('<int:pk>/', ItemDetail.as_view()),  # GET, PUT, DELETE: Item details
    # '<int:pk>'  means that the path is dynamic bc it has a update/remove
]
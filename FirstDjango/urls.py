from django.urls import path

from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('item/<int:item_number>', views.get_items),
    path('items', views.items_list)
]

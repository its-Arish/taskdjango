from django.urls import path
from .views import *

urlpatterns = [
     path("avg-sale/", avg_sale_of_2years),
    path("min-sale/", least_sale_list),
    path("all-data/", viewData, name="data view"),
    path("all-sale/", AllSale),
    path("", landing),
]

from django.urls import path
from .views import get_item, buy_item

urlpatterns = [
    path('item/<int:pk>', get_item),
    path('buy/<int:pk>', buy_item)

]

from django.urls import path
from .views import get_item, buy_item, buy_order, ok, fail

urlpatterns = [
    path('item/<int:pk>', get_item),
    path('buy/<int:pk>', buy_item),
    path('order', buy_order),
    path('success', ok),
    path('cancel', fail)
]

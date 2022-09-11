from django.urls import path
from .views import get_item, buy_item, buy_order, ok, fail

urlpatterns = [
    path('item/<int:pk>', get_item, name='detail'),
    path('buy/<int:pk>', buy_item, name='buy'),
    path('order', buy_order, name='order'),
    path('success', ok, name='ok'),
    path('cancel', fail, name='fail')
]

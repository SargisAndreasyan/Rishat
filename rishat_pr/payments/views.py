import stripe
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import Item


@api_view(('GET',))
def get_item(request, pk):
    item = Item.objects.filter(id=pk).first()
    if item is not None:
        context = {
            'name': item.name,
            'price': item.price,
            'description': item.description,
            'id': pk
        }
        return render(request, template_name='item_detail.html', context=context)
    else:
        return HttpResponse('item.name')

with open('key.txt', 'r') as f:
    stripe.api_key = f.readline()


@api_view(('GET',))
def buy_item(request, pk):
    item = Item.objects.filter(id=pk).first()
    if item is not None:
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=HttpResponse("Покупка удалась"),
            cancel_url=HttpResponse("Покупка не удалась"),
        )
        return redirect(session.url, code=303)

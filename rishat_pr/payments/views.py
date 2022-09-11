import stripe
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import Item
from .forms import OrderForm


def ok(request):
    return HttpResponse('Покупка удалась')


def fail(request):
    return HttpResponse('Покупка не удалась')


def buy(name, price):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': name,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url="https://localhost/success",
        cancel_url="https://localhost/cancel",
    )
    return session


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
        return HttpResponse('Not Found')


with open('key.txt', 'r') as f:
    stripe.api_key = f.readline()


@api_view(('GET',))
def buy_item(request, pk):
    item = Item.objects.filter(id=pk).first()
    if item is not None:
        session = buy(item.name, item.price)
        return redirect(session.url, code=303)


@api_view(('GET', 'POST'))
def buy_order(request):
    if request.method == 'GET':
        return render(request, 'order_buy.html', context={'form': OrderForm})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            items = [item for item in form.cleaned_data.get('items')]
            names = ''
            price = 0
            for item in items:
                names += item.name + ' '
                price += item.price
            session = buy(names, price)
            return redirect(session.url, code=303)

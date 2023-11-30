import stripe
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.conf import settings
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

@require_GET
def get_buy_session(request, id):
    item = get_object_or_404(Item, pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(f'/success/{item.id}'),
        cancel_url=request.build_absolute_uri(f'/cancel/{item.id}'),
    )
    return JsonResponse({'session_id': session.id})

@require_GET
def get_item_page(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'item_detail.html', {'item': item})

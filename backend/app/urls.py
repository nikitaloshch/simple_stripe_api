from django.urls import path
from .views import get_stripe_session, item_detail

urlpatterns = [
    path('buy/<int:item_id>/', get_stripe_session, name='get_stripe_session'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
]


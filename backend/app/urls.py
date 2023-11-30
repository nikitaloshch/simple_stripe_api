from django.urls import path
from .views import get_buy_session, get_item_page

urlpatterns = [
    path('buy/<int:id>/', get_buy_session, name='get_buy_session'),
    path('item/<int:id>/', get_item_page, name='get_item_page'),
]

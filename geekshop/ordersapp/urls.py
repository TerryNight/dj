import ordersapp.views as ordersapp
from django.urls import re_path

app_name="ordersapp"

urlpatterns = [
    path('$', ordersapp.OrderList.as_view(), name='orders_list'),
    path('forming/complete/', ordersapp.order_forming_complete, name='order_forming_complete'),
    path('create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('read/', ordersapp.OrderRead.as_view(), name='order_read'),
    path('update/', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/', ordersapp.OrderDelete.as_view(), name='order_delete'),
]

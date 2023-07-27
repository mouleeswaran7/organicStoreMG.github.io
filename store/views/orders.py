from django.shortcuts import render,redirect
from django.views import View
from store.models.orders import Order


class OrderView(View):
    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
def delOrder(request,fid):
    order=Order.objects.get(id=fid)
    order.delete()
    return redirect('/orders')

from django.contrib import admin
from django.urls import path
from .views.home import Index, store, Payview,product_detail
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView,delOrder
from .views.Intropage import Intropage
from .middlewares.auth import  auth_middleware
from django.urls import path

urlpatterns = [
    path('intro',Intropage),
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('delOrder/<int:fid>',delOrder,name='delfood'),
    path('p_detail/<int:pid>',product_detail,name='pdetails'),
    path('pay/<int:pid>',Payview, name='pay'),




]

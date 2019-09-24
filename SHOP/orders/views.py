from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
from carts.models import Cart
from .models import Order
from .utils import id_generator


def orders(request):
    context = {}
    template = 'orders/user.html'
    return render(request, template, context)


@login_required
def checkout(request):

    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("view"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse("view"))

    if new_order.status == "Finished":
        del request.session['cart_id']
        del request.session['items_total']
        return HttpResponseRedirect(reverse("view"))

    context = {}
    template = "products/home.html"
    return render(request, template, context)

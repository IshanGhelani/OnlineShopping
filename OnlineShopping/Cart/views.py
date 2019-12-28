import datetime

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Home.models import OrderDetails, ProductDescription, OrderHistory
from django.conf import settings

from Login.models import User


def cart(request):
    try:
        total = 0
        cartdata = OrderDetails.objects.filter(user_id=request.session['uid'])
        for i in cartdata:
            total = total + i.quantity * i.price
        #print(cartdata)
        if total == 0:
            return render(request, 'cart.html', {'msg': 'Your Cart is Empty', 'total': total})
        else:
            return render(request, 'cart.html', {'cart': cartdata, 'total': total})
    except KeyError:
        return render(request, 'login.html', {'msg': 'Login to view your Cart!'})


def pay(request):
    return render(request, 'payment.html')


def bill(request):
    try:
        x = request.session['id']
        total = 0
        uid = request.session['uid']
        cart = OrderDetails.objects.filter(user_id=uid)
        for i in cart:
            total = total + i.quantity * i.price
        return render(request, 'bill.html', {'bill': cart, 'total': total})
    except KeyError:
            return render(request, 'login.html', {'msg': 'Login to view bill !'})


def place(request):
    try:
        msg = 'hello ' + request.session['name'] + '\n\n\n'
        uid = request.session['uid']
        op = OrderDetails.objects.filter(user_id=uid)
        user = User.objects.get(id=request.session['id'])
        if op.count() == 0:
            return render(request, 'index.html', {'msg': 'Invalid Access! '})

        for i in op:
            j = OrderHistory(
                user_id=i.user_id,
                o_date=datetime.datetime.now(),
                price=i.price,
                p_id=i.p_id,
                quantity=i.quantity,
                images=i.images,
                item=i.item,
            )
            msg = msg + 'Item : ' + str(i.item) + '\tQuantity : ' + str(i.quantity) + '\tprice : ' + str(i.quantity * i.price) + '\n'
            j.save()
            i.delete()

        subject = 'order confirm message.'
        message = msg + '\n\n\n\n' + 'thank you for shopping with us...' + '\n' + ' - Developer Team' + '\n'
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]

        #print(message)

        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return render(request, 'index.html', {'msg1': 'Your Order Placed Successfully! '})
    except KeyError:
        return render(request, 'login.html', {'msg': 'Login to place order !'})


def history(request):
    try:
        h = OrderHistory.objects.filter(user_id=request.session['uid'])
        return render(request, 'history.html', {'history': h})
    except KeyError:
        return render(request, 'login.html', {'msg': 'login to view History'})


def add(request):
    try:
        uid = request.session['uid']
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        if int(quantity) < 1:
            return render(request, 'index.html', {'msg': 'Cannot add to cart'})

        qu = ProductDescription.objects.get(p_id=item)
        price = qu.price
        for i in OrderDetails.objects.all():
            if i.p_id == qu and uid == i.user_id:
                i.quantity = int(i.quantity) + int(quantity)
                i.save()
                return HttpResponseRedirect('/Cart/')
        q = OrderDetails(
            user_id=uid,
            o_date=datetime.datetime.now(),
            price=price,
            p_id=qu,
            quantity=quantity,
            images=qu.images,
            item=qu.item,
        )
        q.save()
        return HttpResponseRedirect('/Cart/')
    except KeyError:
        return render(request, 'login.html', {'msg': 'Please Login to Modify your Cart!'})
    except ValueError:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request):
    uid = request.session['uid']
    item = request.POST.get('item')
    qu = ProductDescription.objects.get(id=item)
    for i in OrderDetails.objects.all():
        if i.p_id == qu and uid == i.user_id:
            i.delete()
            return HttpResponseRedirect('/Cart/')
    return HttpResponseRedirect('/Cart/')


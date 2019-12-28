from random import randint
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import csrf
from .models import User
from twilio.rest import TwilioRestClient
from twilio.rest import Client


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def create(request):
    try:
        x = request.session['id']
        return render(request, 'index.html', {'msg1': 'You already have an Account !'})
    except KeyError:
        return render(request, 'create.html')


# def verification(request):
#    return render(request, 'notification.html')


def register(request):
    try:
        uname = request.POST.get('uname', '')
        uid = request.POST.get('uid', '')
        password = request.POST.get('pass', '')
        cpass = request.POST.get('cpass', '')
        phnum = request.POST.get('phnum', '')
        email = request.POST.get('mail', '')
        gender = request.POST.get('gen', '')
        address = request.POST.get('address', '')
        for i in User.objects.all():
            if uid == i.user_id:
                return render(request, 'create.html', {'msg': 'UserID is Already Taken'})
        if password != cpass:
            return render(request, 'create.html', {'msg': 'Your both Passwords are different'})
        else:
            q = User(
                user_name=uname,
                user_id=uid,
                password=password,
                ph_number=phnum,
                email=email,
                gender=gender,
                address=address,
            )
            q.save()
            return render(request, 'login.html', {'msg1': 'Your Account is ready! please login to enjoy Shopping'})
    except ValueError:
        return render(request, 'index.html', {'msg': 'invalid access !'})


def forgot(request):
    c = {}
    c = c.update(csrf(request))
    return render(request, 'forgot.html', c)


'''
    account_sid = "ACa4f0d15dce36666d2308113334d407a1"
    auth_token  = "b24c67c428ee871a65be20a5eab69c56"
    client = TwilioRestClient(account_sid, auth_token)
    
    message = client.messages.create(
        body="Generated Temp",
        to="+917990443746",
        from_="+15132943350",
        media_url="http://www.example.com/hearts.png"
    )
    print message.sid
'''


def forgott(request):
    try:
        c = {}
        c = c.update(csrf(request))
        otp = randint(100000, 999999)
        request.session['detail'] = request.POST.get('forg')
        request.session['otp'] = otp
        try:
            target = User.objects.get(email=request.session['detail'])

            subject = 'Forgot Password ?'
            message = '\nYour One Time Password is : ' + str(
                otp) + '\nplease verify to change password\n\nThank you for supporting Us\n'
            from_email = settings.EMAIL_HOST_USER
            to_list = [request.session['detail']]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        except User.DoesNotExist:
            try:
                target = User.objects.get(ph_number=request.session['detail'])

                account_sid = "ACa4f0d15dce36666d2308113334d407a1"
                auth_token = "b24c67c428ee871a65be20a5eab69c56"
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body='\nYour One Time Password is : ' + str(otp) + '\nplease verify to change password\n\nThank you for supporting Us\n',
                    to=str(request.session['detail']),
                    from_="+15132943350",
                    # from_="+917990443746",
                    # media_url="http://www.example777.com/abc/",
                )
                print(message.sid)

            except User.DoesNotExist:
                return render(request, 'login.html', {'msg': 'Your Email is not registered'})
        return render(request, 'forgot2.html', c)
    except ValueError:
        return render(request, 'login.html', {'msg': 'Not registered'})


def verify(request):
    uid = request.POST.get('uid', '')
    password = request.POST.get('pass', '')
    for i in User.objects.all():
        if uid == i.user_id and password == i.password:
            request.session['name'] = i.user_name
            request.session['id'] = i.id
            request.session['uid'] = i.user_id
            return HttpResponseRedirect('/Home/')
    else:
        return render(request, 'login.html', {'msg': 'Wrong user id or password'})


def change(request):
    otp = request.session['otp']
    if otp == int(request.POST.get('otp')):
        return render(request, 'changepass.html')
    else:
        return render(request, 'login.html', {'msg': 'Verification Failed!'})


def verifyt(request):
    password = request.POST.get('pass', '')
    cpass = request.POST.get('cpass', '')
    if password != cpass:
        return render(request, 'login.html', {'msg': 'Can not change password. Your both Passwords are different'})
    else:
        try:
            target = User.objects.get(email=request.session['detail'])
        except User.DoesNotExist:
            target = User.objects.get(ph_number=request.session['detail'])
        target.password = password
        target.save()
        del request.session['detail']
        return render(request, 'login.html', {'msg1': 'Password successfully changed. Please login to enjoy shopping'})


def logout(request):
    del request.session['name']
    del request.session['id']
    del request.session['uid']
    return HttpResponseRedirect('/Home/')


def profile(request):
    try:
        i = User.objects.get(user_id=request.session['uid'])
        return render(request, 'profile.html', {'i': i})
    except KeyError:
        return render(request, 'login.html', {'msg': 'Please Login to view Profie'})


def update(request):
    try:
        i = User.objects.get(user_id=request.session['uid'])
        return render(request, 'update.html', {'i': i})
    except KeyError:
        return render(request, 'login.html', {'msg': 'you can\'t update profile without login!'})


def updatet(request):
    uname = request.POST.get('uname', '')
    uid = request.POST.get('uid', '')
    password = request.POST.get('pass', '')
    cpass = request.POST.get('cpass', '')
    phnum = request.POST.get('phnum', '')
    email = request.POST.get('mail', '')
    gender = request.POST.get('gen', '')
    address = request.POST.get('address', '')
    if password != cpass:
        return render(request, 'update.html', {'msg': 'Your both Passwords are different'})
    else:
        User.objects.filter(id=request.session['id']).delete()
        for i in User.objects.all():
            if uid == i.user_id:
                return render(request, 'update.html', {'msg': 'UserID is Already Taken'})
        q = User(
            user_name=uname,
            user_id=uid,
            password=password,
            ph_number=phnum,
            email=email,
            gender=gender,
            address=address,
        )
        q.save()
        request.session['name'] = uname
        request.session['id'] = q.id
        request.session['uid'] = q.user_id

        i = User.objects.get(user_id=request.session['uid'])
        return render(request, 'profile.html', {'i': i, 'msg1': 'Your data has been updated!'})

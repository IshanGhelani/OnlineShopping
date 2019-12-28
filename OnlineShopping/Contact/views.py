from django.http import HttpResponseRedirect
from django.shortcuts import render

from Login.models import User
from .models import Feedback


def feed(request):
    email = request.POST.get('email', '')
    feedback = request.POST.get('feedback', '')
    for i in Feedback.objects.all():
        if email == i.email:
            return render(request, 'index.html', {'msg': 'feedback already given '})
    q = Feedback(
        email=email,
        feedback=feedback,
    )
    q.save()
    return render(request, 'index.html', {'msg1': 'Thank you for your valuable feedback '})


def cont(request):
    try:
        x = request.session['id']
        y = User.objects.get(id=x)
        return render(request, 'contact.html', {'user': y})
    except KeyError:
        return render(request, 'contact.html')
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


def logview(request):
    return render(request, 'description.html')
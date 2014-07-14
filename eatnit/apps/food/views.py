from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
#from eatnit.eatnit_app.models import Meal,Restaurant,MealServed

from django.template import RequestContext, loader
# Create your views here.


def index(request):
    # meal_list = Meal.objects.order_by('name')
    context = RequestContext(request, {
         #'meal_list': meal_list,
    })


    messages.add_message(request, messages.INFO, 'Hello world.')
    
    return render(request, 'index.html', context)
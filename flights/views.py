from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, flight, Passenger
from django.views import View
from django.views.generic import ListView
from django.core.mail import send_mail
from django import forms
from django.forms import ModelForm

"""# class
class my_form(forms.Form):
    num1 = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 50, 'class': 'my_class'}
    ))
    num2 = forms.IntegerField()
"""

# Create your views here.
"""def index(request):
    if request.method == "GET":
        new_form = my_form()
        return render(request, "flights/flight.html", {'form': new_form})
    else:
        # Make a bound form
        submitted_form = my_form(request.POST)
        # Validate data
        if submitted_form.is_valid():
            # access cleaned_data[] if valid
            num1 = submitted_form.cleaned_data['num1']
            num2 = submitted_form.cleaned_data['num2']
            return HttpResponse(num2 + num1)
        else:
            # Data invalid
            return render(request, 'flights/flight.html', {'form': submitted_form})
        return HttpResponse('Success')
 """

 # Model forms
class flightForm(ModelForm):
    class Meta:
        model = flight
        fields = ['origin', 'destination', 'duration']



def index(request):
    if request.method == "GET":
        new_form = flightForm()
        return render(request, 'flights/flight.html', {'form': new_form})
    if request.method == "POST":
        submitted_form = flightForm(request.POST)
        if submitted_form.is_valid():
            submitted_form.save()
        else:
            pass
    return HttpResponse('Success')
    

def flight_(request, flight_id):
    my_flight = flight.objects.all().filter(id__exact=flight_id)[0]
    my_passengers = Passenger.objects.all().filter(flights=my_flight)
    return render(request, 'flights/flight.html', {'flight': my_flight, 'passengers': my_passengers})

def my_sessions(request):
    request.session['variable'] = [10,20,30]
    text = request.session['variable']
    del request.session['variable']
    return HttpResponse(text)
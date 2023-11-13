from django.shortcuts import redirect, render
from finance.models import DonationMethod
from .models import *
from .forms import *
# Create your views here.


def trainings(request):
    
    
    course = Course.objects.all()
    track = Track.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        'testimonial': testimonial,
        'course': course,
        'track': track,
        'form': studentform
    }
    return render(request, 'edu/edu.html', context)




def studentpage(request):
    if request.POST:
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(registeredpage)
    
    
    context = {
        'form': studentform
    }
    return render(request, 'edu/studentsform.html', context)


def registeredpage(request):
    price = Course.objects.all()
    donation_method = DonationMethod.objects.all()
    context = {
        'price': price,
        'donation_method': donation_method,

    }
    return render(request, 'edu/registeredpage.html', context)


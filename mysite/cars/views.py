from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ReviewForm


# Create your views here.


def review(request): 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))
    else:
        form = ReviewForm()
    return render(request, 'cars/review.html',{'form':form})


def thank_you(request):
    return render(request, 'cars/thank_you.html')
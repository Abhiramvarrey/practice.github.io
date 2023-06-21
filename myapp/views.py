from django.shortcuts import render
from .forms import newuser


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    sign=newuser()
    if request.method == 'POST':
        sign = newuser(request.POST)
        if sign.is_valid():
            sign.save(commit=True)
            return home(request)
        else:
            return render(request, 'signup.html')
    return render(request,'signup.html',{'signup':sign})
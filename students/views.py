from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('session-view')
    else:
        return HttpResponse('<p> Oops.. you are not logged in as student !! </p>')
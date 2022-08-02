from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentor
import simplejson as json
from datetime import datetime


# Create your views here.
def home_view(request):
    context = {}
    mentors = Mentor.objects.all()
    jsonDec = json.decoder.JSONDecoder()
    if request.user.is_authenticated and request.user.is_staff:
        l_data =  map(lambda x: { 'subjects' : jsonDec.decode(x.subjects),'dates': jsonDec.decode(x.timeslots), 'name': x.ref.username }, mentors)
        active_mentor = mentors.get( ref = request.user )
        context['active_mentor'] = active_mentor.ref.username
        context['mentors'] = list(l_data)
        t = context['mentors'][0]
        print(type(t['subjects']),type(t['dates']))
        return render(request,'mentors/home.html', context)
    else:
        msg = 'Oops.. cannot access this site here, You need to be logged in as mentor to access this site!!'
        context['msg'] = msg
        return render(request,'mentors/home.html', context)

# What type of request is it
# Who is allowed to make the request or the paths that can access it
# Who is the view for
# Which sections are restricted to which users
# What is the current active user
# Wheather redirection or rendering needs to happen

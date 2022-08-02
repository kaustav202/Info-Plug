from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from mentors.models import Mentor
from students.models import Student
from .models import Session
import simplejson as json
import datetime
from datetime import timedelta
from datetime import datetime as dt

# Create your views here.

# Tasks remaining : Reschedule Buttons , Mentor View Context, Slot Calculation Technique, API Endpoints

def session_manager(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        mentors = Mentor.objects.all()
        user = request.user
        student = Student.objects.get(name=user.username)
        jsonDec = json.decoder.JSONDecoder()
        format_str = "%Y-%m-%d %H:%M:%S"
        for mentor in mentors:
            subjects = jsonDec.decode(mentor.subjects)
            if subject in subjects:
                assigned = mentor.ref.username
                timeslots =  jsonDec.decode(mentor.timeslots)
                last_slot = timeslots[-1]
                slot_decoded = dt.strptime(last_slot,format_str)
                booked_slot = slot_decoded + timedelta(minutes=30)
                booked_slot_encoded = booked_slot.strftime(format_str)
                timeslots.append(booked_slot_encoded)
                times
                
                
                
                
                
                
                
                
                
                
                
                
                lized = json.dumps(timeslots)
                mentor.timeslots = timeslots_serialized
                mentor.save()
                session = Session(mentor_name=assigned,student_name=student.name,timeslot=booked_slot_encoded,subject=subject,mentor_ref = mentor,student_ref = student)
                session.save()
                break
        sessions = Session.objects.all()
        user_sessions = sessions.filter(student_name = user.username)
        data = []
        for user_session in user_sessions:
            slot = user_session.timeslot
            slot = dt.strptime(slot,format_str)
            us_mentor = user_session.mentor_name
            us_subject = user_session.subject
            d = {"slot": slot,"mentor": us_mentor,"subject": us_subject }
            data.append(d)
        context = {"data": data}
        return render(request, 'scheduleSessions/session.html',context)
    else:
        sessions = Session.objects.all()
        user_sessions = sessions.filter(student_name = request.user.username)
        data = []
        for user_session in user_sessions:
            slot = user_session.timeslot
            slot = jsonDec.decode(slot)
            slot = dt.strptime(slot,format_str)
            us_mentor = user_session.mentor_name
            us_subject = user_session.subject
            d = {"slot": slot,"mentor": us_mentor,"subject": us_subject }
            data.append(d)
        context = {"data": data}
        return render(request, 'scheduleSessions/session.html',context)

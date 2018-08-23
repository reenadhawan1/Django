from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.db import connection


def index(request):
    return render(request,'trip/index.html')

def register(request):
    errors = User.objects.registerValidator(request.POST)
    print(errors)
    if errors:
        for key,val in errors.items():
            messages.error(request,val, extra_tags=key)
        return redirect('/')
    pwHash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name =request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pwHash)
    request.session['first_name'] = request.POST['first_name']
    request.session['id'] = user.id
    return redirect('/travels/')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if errors:
        for key,val in errors.items():
            messages.error(request,val, extra_tags=key)
        print(errors)
        return redirect('/')
    user = User.objects.get(email = request.POST['login_email'])
    request.session['first_name'] = user.first_name
    request.session['id'] = user.id
    return redirect('/travels/')

def logout(request):
    request.session.flush()
    return redirect('/')


def dashboard(request):
    user = User.objects.get(id =request.session['id'] )
    content = {
        'user_trips': User.objects.raw(f'select trip_trip.id,planner_id, destination,desc,date(start_date) as "start_date",date(end_date) as "end_date" from trip_trip join trip_trip_trip_members on trip_trip.id = trip_trip_trip_members.trip_id where trip_trip_trip_members.user_id = {user.id} union select trip_trip.id,planner_id, destination,desc,date(start_date) as "start_date",date(end_date) as "end_date" from trip_user join trip_trip on trip_user.id = trip_trip.planner_id where trip_user.id = {user.id} '),
        'other_trips': User.objects.raw(f'select tt.id, destination,desc,date(start_date) as start_date,date(end_date) as end_date from trip_trip tt where tt.planner_id != {user.id} and not exists (select 1 from trip_trip_trip_members where trip_trip_trip_members.trip_id = tt.id and  trip_trip_trip_members.user_id = {user.id})')
    }
    return render(request,'trip/dashboard.html',content)

def addTrip(request):

    return render(request,'trip/addtrip.html')

def tripAdd(request):
    errors = User.objects.tripValidator(request.POST)
    if errors:
        for key,val in errors.items():
            messages.error(request,val, extra_tags=key)
        return redirect('/addtrip/')
    user = User.objects.get(id =request.session['id'] ) 
    Trip.objects.create(planner =user,destination = request.POST['dest'],desc = request.POST['desc'],start_date = request.POST['from'],end_date = request.POST['to'])
    return redirect('/travels/')

def join(request,id):
    user = User.objects.get(id =request.session['id'] )
    trip = Trip.objects.get(id=id)
    user.joined_trips.add(trip)
    return redirect('/travels/')

def cancel(request,id):
    trip = trip = Trip.objects.get(id=id)
    user = User.objects.get(id =request.session['id'] )
    cursor = connection.cursor()
    cursor.execute('DELETE FROM trip_trip_trip_members WHERE trip_id = %s and user_id = %s', (trip.id,user.id))
    connection.commit()
    return redirect('/travels/')

def delete(request,id):
    trip = trip = Trip.objects.get(id=id)
    trip.delete()
    return redirect('/travels/')

def trip(request,id):
    content = {
        "trip" : Trip.objects.get(id=id)
    }
    return render(request,'trip/trip.html',content)
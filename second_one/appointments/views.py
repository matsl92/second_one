from django.shortcuts import render, HttpResponse, redirect
from .models import Week, Gap, User, Appointment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from .forms import UserForm, AppointmentForm

@login_required(login_url='/login/')
def home(request):
    context = {}
    return render(request, 'appointments/home.html', context)

def personal_info(request):
    if request.method == 'GET':
        form = UserForm()
        context = {'form': form}
        return render(request, 'appointments/personal_info.html', context)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("don't know what happened")
        return(HttpResponse('there'))
        
def create_gaps(request): 
    dictionary = Week.objects.last().__dict__
    minutes_per_appointment = dictionary['minutes_per_appointment']
    start_date = dictionary['start_date']
    monday = [dictionary['monday_start'], dictionary['monday_end'], 0]
    tuesday = [dictionary['tuesday_start'], dictionary['tuesday_end'], 1]
    wednesday = [dictionary['wednesday_start'], dictionary['wednesday_end'], 2]
    thursday = [dictionary['thursday_start'], dictionary['thursday_end'], 3]
    friday = [dictionary['friday_start'], dictionary['friday_end'], 4]
    saturday = [dictionary['saturday_start'], dictionary['saturday_end'], 5]
    sunday = [dictionary['sunday_start'], dictionary['sunday_end'], 6]
    gap_duration = datetime.timedelta(minutes=minutes_per_appointment)
    week = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
       
    class SemiGap:
        def __init__(self, beginning, end, index, state=False):
            self.beginning = beginning
            self.end = end
            self.index = index
            self.state = state
        
        def __str__(self):
            return str(self.beginning.time())

    gaps_of_week = []
    j = 0
    for day in week:
        gaps_of_day = []  # This list of lists has all the semigaps according to the last instance of Week 
                          # Empty days are empty lists
        try:
            beginning = datetime.datetime(start_date.year, start_date.month, start_date.day, day[0].hour, day[0].minute) + datetime.timedelta(days=day[2])
            end = datetime.datetime(start_date.year, start_date.month, start_date.day, day[1].hour, day[1].minute) + datetime.timedelta(days=day[2])
            n_of_gaps = (end-beginning).seconds // gap_duration.seconds
        except:
            gaps_of_week.append(gaps_of_day)
            j += 1
            continue
        for i in range(n_of_gaps): 
            end = beginning + gap_duration
            semigap = SemiGap(beginning, end, ':'.join([str(j), str(i)]))
            gaps_of_day.append(semigap)               
            beginning = end
        gaps_of_week.append(gaps_of_day)
        j += 1
    
    if request.method == 'GET':
        context = {'gaps_of_week': gaps_of_week}
        return render(request, 'appointments/create_gaps.html', context)
    
    if request.method == 'POST':
        try:
            indexes = dict(request.POST.lists())['indexes']
            # print(indexes)     
        except:
            indexes = []
        week = []
        i = 0
        for day in gaps_of_week:
            gaps_of_day = []
            j = 0
            for semi_gap in day:
                if not str(semi_gap.index) in indexes:
                    time_period = semi_gap.end-semi_gap.beginning
                    gap = Gap(date_and_time=semi_gap.beginning, time_period=time_period, index=':'.join([str(i), str(j)]))
                    gaps_of_day.append(str(gap.date_and_time.time()))
                    
                    # gap.save()       # keep saving gaps
                    
                j += 1       
            i += 1
            week.append(gaps_of_day) 
                              
        # for gap in Gap.objects.all():  # delete 
        #     gap.delete()               # all gaps
            
        context = {'week': week}
        return render(request, 'appointments/created_gaps.html', context)
    
def gaps(request):
    if request.method == 'GET':
        try:
            earliest_day = Gap.objects.all().order_by('date_and_time')[0].date_and_time # This is a datetime object
            all_gaps = []
            for i in range(7):
                current_datetime = earliest_day+datetime.timedelta(days=i)
                all_gaps.append(Gap.objects.filter(date_and_time__year=current_datetime.year).filter(date_and_time__month=current_datetime.month).filter(date_and_time__day=current_datetime.day))
            context = {'all_gaps': all_gaps}
            return render(request, 'appointments/gaps.html', context)
        except:
            return HttpResponse('There are no available timeslots')
    
    if request.method == 'POST': 
        # print(request.POST)
        index = dict(request.POST.lists())['index'][0]
        earliest_day = Gap.objects.all().order_by('date_and_time')[0].date_and_time # This is a datetime object
        all_gaps = []
        for i in range(7):
            current_datetime = earliest_day+datetime.timedelta(days=i)
            all_gaps.append(Gap.objects.filter(date_and_time__year=current_datetime.year).filter(date_and_time__month=current_datetime.month).filter(date_and_time__day=current_datetime.day))
        for daily_gaps in all_gaps:
            for gap in daily_gaps:
                if str(gap.index) == index:
                    date_and_time = gap.date_and_time              
                    time_period = gap.time_period
                    index = gap.index            
                    break
        form = UserForm()
        context = {'index': index, 
                   'form': form, 
                   'date': date_and_time.date(),
                   'time': date_and_time.time(), 
                   'date_and_time': date_and_time, 
                   'time_period': time_period, 
                   }
        return render(request, 'appointments/schedule.html', context)

def success(request):
    print(request.POST)
    return HttpResponse('creating your appointment')
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import CreateExerciseForm



def index(request, year=datetime.now().year, month=datetime.now().month):
    cal = HTMLCalendar().formatmonth(year, month)
    now = f"{datetime.now().day} {datetime.now().strftime('%B')}, {datetime.now().year}"
    context = {  
        'year': year,
        'month': month,
        "cal": cal,
        'now': now
    }
    
    return render(request, "index.html", context)
  
  
def workout_list(request):
    workouts = Workout.objects.all()
    exercises = Exercise.objects.all()
    context = {'workouts': workouts, 'exercises': exercises}
    return render(request, 'workout-list.html', context)


def exercise_list(request):
    exercises = CreateExercise.objects.all()
    form = CreateExerciseForm()
    context = {'exercises': exercises, 'form': form}
    return render(request, 'exercise-list.html', context)


def new_exercise(request):
    exercises = CreateExercise.objects.all()
    if request.method == 'POST':
        
        form = CreateExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save()
            context = {'exercise': exercise, 'exercises': exercises}
            return render(request,'partials/new-exercises.html', context)
        
    form = CreateExerciseForm()
    context = {'form': form, 'exercises': exercises}   
    return render(request,'partials/new-exercises.html', context)
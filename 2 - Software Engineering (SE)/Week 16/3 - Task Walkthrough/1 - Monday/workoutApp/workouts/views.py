from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .forms import WorkoutForm


def get_all(request):
    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
        'page_title': 'Workouts'
    }

    return render(request, 'workouts/index.html', context)

def get(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/detail.html', {'workout': workout})

def create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)

        if form.is_valid():
            workout = form.save(commit=False)
            workout.save()
            return redirect('workouts')
        
    else:
        form = WorkoutForm()

    return render(request, 'workouts/workout_form.html', {'form': form})

def update(request, pk):
    workout = get_object_or_404(Workout, pk=pk)

    if (request.method == 'POST'):
        form = WorkoutForm(request.POST, isntance=workout)

        if form.is_valid():
            workout = form.save(commit=False)
            workout.save()
            return redirect('workouts')
        
    else:
        form = WorkoutForm(instance=workout)

    return render(request, 'workouts/workout_form.html', {'form': form})

def delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    workout.delete()
    return redirect('workouts')

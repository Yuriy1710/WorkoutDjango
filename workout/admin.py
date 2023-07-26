from django.contrib import admin
from .models import *


class ExerciseInline(admin.TabularInline):
    model = Exercise

class WorkoutAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(CreateExercise)
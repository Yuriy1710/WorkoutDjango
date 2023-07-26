from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/<str:month>/', views.index, name='index'),
    path('workout-list/', views.workout_list, name="workout_list"),
    path('exercise-list/', views.exercise_list, name="exercise_list"),
    path('new-exercises/', views.new_exercise, name="new_exercise"),
]

from django.db import models



class Workout(models.Model):
   
    date = models.DateField()
    
    def __str__(self):
        return f"{self.date}"



class CreateExercise(models.Model):
    name = models.CharField(max_length=250)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, blank=True, null=True)    
    
    def __str__(self):
        return self.name



class Exercise(models.Model):
    name = models.ForeignKey(CreateExercise, on_delete=models.CASCADE, blank=True, null=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    sets = models.PositiveSmallIntegerField(default=3)
    reps = models.PositiveIntegerField(default=10)
    
    def __str__(self):
        return f"{self.name} - {self.weight} - {self.sets} - {self.reps}"
      
      


    

from django.db import models

# Create your models here.
class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    # departure, arrivals

    def __str__(self):
        return str(self.city)

class flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()

    def __str__(self):
        return str(self.origin) + " to " + str(self.destination)
    
class Passenger(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    flights = models.ManyToManyField(flight)

    def __str__(self):
        return str(self.fname) + " " + str(self.lname)






    
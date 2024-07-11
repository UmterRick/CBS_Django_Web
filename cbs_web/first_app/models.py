from django.db import models


# Create your models here.
class Passenger(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=170)
    email = models.EmailField(unique=True)


class Employee(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    position = models.CharField(max_length=50, choices=[("pilot", "Pilot"), ("manager", "Manager"), ("stuart", "Flight Attendant")])


class Plane(models.Model):
    id = models.UUIDField(primary_key=True)
    serial_number = models.PositiveIntegerField(unique=True),
    model = models.CharField(max_length=20)
    seats = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)


class Flight(models.Model):
    id = models.UUIDField(primary_key=True)
    destination = models.CharField(max_length=30)
    departure = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    plane = models.ForeignKey(to=Plane, on_delete=models.RESTRICT)
    personal = models.ManyToManyField(Employee)


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True)
    flight = models.ForeignKey(to=Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(to=Passenger, on_delete=models.CASCADE)
    seat = models.CharField(max_length=5)
    type = models.CharField(max_length=15, choices=[("E", "Econom"), ("S", "Standard"), ("F", "First_clas"), ("B", "Business")])
    gate = models.PositiveSmallIntegerField()



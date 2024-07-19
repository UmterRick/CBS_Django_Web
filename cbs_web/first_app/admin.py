import django.forms
from django.contrib import admin

from .models import Plane, Ticket, Passenger, Employee, Flight


# Register your models here.

@admin.register(Plane)
class PlanesAdmin(admin.ModelAdmin):
    list_display = ["model", "serial_number", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["id"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    ...


class FlightAdminCreateForm(django.forms.ModelForm):
    model = Flight
    fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["plane"].queryset = Plane.objects.filter(is_available=True)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    form = FlightAdminCreateForm


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ...


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    ...

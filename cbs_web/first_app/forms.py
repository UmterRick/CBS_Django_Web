import datetime

from django import forms

from first_app.models import Employee, Ticket

suffix = "CBS :"


class SomeForm(forms.Form):
    name = forms.CharField(required=True, initial="Name_1", error_messages={
        "required": "Field name cant be empty"
    }, label_suffix=suffix)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True, initial="@gmail.com", label="User Email", label_suffix=suffix)
    height = forms.IntegerField(min_value=50, max_value=300, step_size=5, help_text="Height in cm")
    birth_date = forms.DateField(initial=datetime.date.today())
    user_type = forms.ChoiceField(choices=(("1", "guest"), ("4", "manager"), ("3", "editor"), ("2", "admin")))
    is_agree = forms.BooleanField(initial=False)
    profile_avatar = forms.ImageField(allow_empty_file=False)
    experience = forms.DurationField()
    unused_field = forms.CharField(disabled=True, required=False)


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"


class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ("seat", "type", "gate", "passenger")


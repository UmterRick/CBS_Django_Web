import datetime

from django.db.models.signals import post_init
from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.views.generic import View

from django.shortcuts import render, redirect

from .forms import TicketForm
from .models import Plane, Flight, Passenger, Ticket


# Create your views here.
def index(request):
    return HttpResponse("Hello, world ! Ви на сторінці 1 уроку.")


def html_response(request):
    return HttpResponse("""
    <p><i>Hello World!</i></p>

    <p><b>Django є одним з найбільших framework на Python</b></p>

    <hr>
""")


def get_all_news(request):
    news_list = [
        "Content 1 too many words",
        "Content words 2",
        "Content 3",
        "Content 4",
        "Content 5",
    ]
    return render(request, "news.html", context={"news": news_list})


def get_news_by_id(request, news_id):
    if news_id > 100 and not request.user.is_authenticated:
        return HttpResponseForbidden()

    print(f"Get News with id={news_id}", type(news_id))
    return HttpResponse(f"<b> News(id={news_id}) </b>")


def regexp_route(request, news_title):
    print(f"Search for news with title: {news_title}")
    return HttpResponse()


class CommentsView(View):
    def get(self, request):
        print("Get all comments")
        return HttpResponse("All comments")


def app_main_page(request):
    print("Somebody request access to main page")
    page_context = {
        "render_datetime": datetime.datetime.now()
    }
    return render(request=request, template_name="index.html", context=page_context)


def buy_ticket(request, flight_id):
    form = TicketForm(request.POST or None)
    if request.method == "GET":
        return render(request=request, template_name="ticket.html", context={"form": form})
    elif request.method == "POST":
        flight = Flight.objects.get(id=flight_id)
        all_is_ok = form.is_valid()
        if all_is_ok:
            ticket = form.save(commit=False)
            ticket.flight = flight
            ticket.save()
            return redirect("app_main_page")
        return render(request=request, template_name="ticket.html", context={"form": form})


def create_new_plane(request):
    # Method 1
    # p = Plane(serial_number=4875, model="Boeing", seats=250, is_available=False)
    # p.save()

    # Method 2
    Plane.objects.create(serial_number=1111, model="Boeing 2", seats=130, is_available=True)
    return HttpResponse(status=200)



def get_flights(request, **kwargs):
    flights = Flight.objects.all()
    return render(request, "flights.html", context={"flights": flights})

def receiver_example(**kwargs):
    print("Post init happened")
    print(kwargs)


post_init.connect(receiver=receiver_example)
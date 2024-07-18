import datetime

from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.views.generic import View

from django.shortcuts import render, redirect

from forms import SomeForm, EmployeeForm, TicketForm


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


def render_some_form(request):
    form = TicketForm(request.POST or None)
    if request.method == "GET":
        return render(request=request, template_name="user_form.html", context={"form": form})
    elif request.method == "POST":
        all_is_ok = form.is_valid()
        if all_is_ok:
            return redirect("app_main_page")
        return render(request=request, template_name="user_form.html", context={"form": form})

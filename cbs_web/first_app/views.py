from http import HTTPStatus

from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.views.generic import View

# from django.shortcuts import render

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
    return HttpResponse()


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


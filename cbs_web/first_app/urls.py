from django.urls import path, re_path

from first_app import views

urlpatterns = [
    path("", views.app_main_page, name="app_main_page"),
    path('lesson-1', views.index, name="index_page"),
    path('lesson-1/hw', views.html_response, name="html_page"),
    path('news', views.get_all_news, name="news_page"),
    path('news/<int:news_id>', views.get_news_by_id),  # app/news/1
    re_path('^news/(?P<news_title>[a-zA-Z0-9]{5})', views.regexp_route),
    path('comments', views.CommentsView.as_view()),
    path('create-plane', views.create_new_plane),
    path('flights', views.get_flights),
    path('ticket?<uuid:flight_id>', views.buy_ticket, name="buy_ticket"),


]

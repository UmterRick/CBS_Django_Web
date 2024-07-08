from django.urls import path, re_path

from first_app import views

urlpatterns = [
    path('lesson-1', views.index, name="index_page"),
    path('lesson-1/hw', views.html_response, name="html_page"),
    path('news', views.get_all_news),
    path('news/<int:news_id>', views.get_news_by_id),  # app/news/1
    re_path('^news/(?P<news_title>[a-zA-Z0-9]{5})', views.regexp_route),
    path('comments', views.CommentsView.as_view()),

]

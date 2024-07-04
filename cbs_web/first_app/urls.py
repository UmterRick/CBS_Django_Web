from django.urls import path

from first_app import views

urlpatterns = [
    path('lesson-1', views.index, name="index_page"),
]

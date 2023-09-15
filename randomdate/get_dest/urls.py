from django.urls import path

from get_dest import views


urlpatterns = [
    path("/", views.snippet_new, name="snippet_new"),
]
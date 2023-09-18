from django.urls import path

from get_dest import views


urlpatterns = [
    # path("/", views., name="snippet_new"),
    # path("/get_dest/top.html", views.top, name="top"),
    path("", views.get_dest ,name="get_dest")
]
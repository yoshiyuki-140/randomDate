from django.urls import path

from get_dest import views


urlpatterns = [
    path("dest/<int:dest_id>", views.dest ,name="dest"),
    # path("dest/", views.dest ,name="dest"),
]
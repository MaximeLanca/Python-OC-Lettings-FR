"""Root URL configuration for the oc_lettings_site project."""

from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = "oc_lettings_site.views.page_not_found"
handler500 = "oc_lettings_site.views.server_error"

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("letting.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]

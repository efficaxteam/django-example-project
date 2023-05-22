from django.urls import path, include

urlpatterns = [
    path("v0/", include("api.v0.urls")),
]

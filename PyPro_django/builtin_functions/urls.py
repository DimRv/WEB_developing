from django.urls import path
from .views import index, details


app_name = "builtin_functions"
urlpatterns = [
    path("", index, name='index'),
    path("<str:func_name>", details, name="details"),
]

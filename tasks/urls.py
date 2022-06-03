from unicodedata import name
from django.urls import URLPattern
from django.urls import path

from . import views

# we use the app name to specify this taks to prevent django conflicts in case other apps have the same name in the paths. uniquiliy will identify this app

app_name = "tasksNC"
#   
urlpatterns = [

    path("", views.index, name="index"),
    path("add", views.add, name="add"),
]
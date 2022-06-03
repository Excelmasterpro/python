from unicodedata import name
from django.urls import URLPattern
from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("nc2", views.ncfunction, name="nc"),
    path("yadi", views.yadi1, name="yadi"),

    path("index2", views.index2, name="index2"),
# if I use the bellow, i'll be able to access the new function created: http://127.0.0.1:8000/hello/nc2
# Then name="" is for later reference and make it easier to refernce


 path("<str:name>", views.greet2, name="greet2"),
    path("<str:name>", views.greet, name="greet")
    
    # the above will take any path we could think: http://127.0.0.1:8000/hello/palabraCualquiera

   
]
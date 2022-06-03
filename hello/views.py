from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("1.Nathan says: Hello, world! God is so Good! Thanks for everything!")


def ncfunction(request):
    return HttpResponse("2. Mark says: Amazing Good you are! Jesus is King!")

def yadi1(request):
    return HttpResponse("3. Yadi says: Jesus healed me")

# render complete html files

def index2(request):
    return render(request, "hello/index.html")




# instead of defining multiple functions, we can add placeholders.

def greet(request, name):
    return HttpResponse(f"5. {name.capitalize()} says: God is the most amazing ever! Jesus reigns")

# now we can return and create htmls

def greet2(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        })



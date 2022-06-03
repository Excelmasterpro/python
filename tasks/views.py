from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

# the problem with using global variables is that every person that has acess to the website will be able to see the same tasks. We usually don't want that. Django has another way of dealing with this, calles "SESSIONS", so every user get's a unique sessions and it's remembered by django for that, we'll delete the tasks array below. But we also have to run a command thorugh the terminal:  python3 manage.py migrate in order to create a table inside django to store the data

# tasks = ["foo", "bar", "baz"] 

  # Django has also built in capabilities to quickly create forms and we dont' have to use the raw html for that
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Django will even make some validations to the form and show to user, only client side validation.

def index(request):
# here we add a new array of tasks in case there is none in the session
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {

        # "tasks": tasks
        "tasks": request.session["tasks"]

    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"] += [task]
            # Django has another built in functionality to send the user back to the prievious url. It's a good practice not to hard code urls, since those might change, hence, we use the below and we also have to import the library fot httpresponse and reverse
            return HttpResponseRedirect(reverse("tasksNC:index")) 

        else:
            return(request, "tasks/add.html", {
                "form": form
            })
    
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

  
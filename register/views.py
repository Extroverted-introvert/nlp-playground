from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from register.forms import CustomUserCreationForm

# Create your views here.

def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "register/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard:dashboard"))
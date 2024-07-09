from django.shortcuts import render
from django.conf import settings
from datetime import date

# Create your views here.

def index(request):
    current = date.today()
    try:
        birthday = settings.BIRTHDAY
    except:
        birthday = (2, 9)
    birth = (current.month, current.day) == birthday
    return render(request, "index.html", {
        "birthday": birth
    })
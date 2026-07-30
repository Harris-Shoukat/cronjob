from django.shortcuts import render
from .models import DummyUser, DateRecord


def home(request):
    return render(request, "scheduler/home.html")


def users(request):
    users = DummyUser.objects.all()

    return render(
        request,
        "scheduler/users.html",
        {
            "users": users
        }
    )


def datetimes(request):
    records = DateRecord.objects.all()

    return render(
        request,
        "scheduler/datetimes.html",
        {
            "records": records
        }
    )
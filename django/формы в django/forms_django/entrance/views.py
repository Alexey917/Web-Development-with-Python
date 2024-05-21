import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.
def index(request):
    counter = 0
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            login = user_form.cleaned_data["login"]
            password = user_form.cleaned_data["password"]
            admin = Admin.objects.all()
            user = User.objects.all()
            for item in admin:
                counter += 1
                if item.login == login and item.password == password:
                    counter = 0
                    return HttpResponse(f'<h2>Здравствуйте, администратор {item.login}</h2>')

            for item in user:
                counter += 1
                if login == item.login and password == item.password:
                    counter = 0
                    return HttpResponse(f"<h2>Здравствуйте, пользователь {item.login}!</h2>")

            if counter > 0:
                return HttpResponse(f"<h2>Неправильные входные параметры!</h2>")

    else:
        user_form = UserForm()
        return render(request, "entrance/index.html", {"form": user_form})


def numbers(request):
    if request.method == "POST":
        first = request.POST.get("first")
        second = request.POST.get("second")
        third = request.POST.get("third")
        action = request.POST.get("action")
        if action == 'min_n':
            minimum = min(int(first), int(second), int(third))
            return HttpResponse(f'<h1>Минимальное число из трех: {minimum}</h1>')
        elif action == 'max_n':
            maximum = max(int(first), int(second), int(third))
            return HttpResponse(f'<h1>Максимальное число из трех: {maximum}</h1>')
        else:
            mid = (int(first) + int(second) + int(third)) / 3
            return HttpResponse(f'<h1>Среднеарифметическое из трех: {mid}</h1>')
    else:
        numbers_form = NumbersForm()
        return render(request, "entrance/numbers.html", {"form": numbers_form})


def registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        address = request.POST.get("address")

        user = {
            "name": name,
            "surname": surname,
            "age": age,
            "email": email,
            "gender": gender,
            "address": address
        }

        registration_form = Registration()
        #return HttpResponse(f'<h1>{user}</h1>')
        return render(request, "entrance/registration.html", context={"user": user,
                                                                      "form": registration_form})

    else:
        registration_form = Registration()
        return render(request, "entrance/registration.html", {"form": registration_form})


def date_programmer(request):
    if request.method == "POST":
        year = request.POST.get("year")

        start_date = datetime.date(int(year), 1, 1)
        end_date = start_date + datetime.timedelta(days=255)
        day = end_date.day
        day_week = end_date.weekday()

        days = [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье",
        ]

        for i in range(len(days)):
            if day_week == i:
                day_week = days[i]

        programmer_form = DateProgrammer()
        return render(request, "entrance/date.html", {"form": programmer_form,
                                                      "day_week": day_week,
                                                      "day": day})

    else:
        programmer_form = DateProgrammer()
        return render(request, "entrance/date.html", {"form": programmer_form})


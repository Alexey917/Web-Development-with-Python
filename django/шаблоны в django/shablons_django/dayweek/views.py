from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    day = ''
    current_date = datetime.date.today().weekday()
    days = [
        {"name_day": "Понедельник", "bg": "green"},
        {"name_day": "Вторник", "bg": "blue"},
        {"name_day": "Среда", "bg": "orange"},
        {"name_day": "Четверг", "bg": "red"},
        {"name_day": "Пятница", "bg": "ocean"},
        {"name_day": "Суббота", "bg": "lime"},
        {"name_day": "Воскресенье", "bg": "purple"},
    ]
    for i in range(len(days)):
        if current_date == i:
            day = days[i]
    return render(request, 'dayweek/index.html', context=day)

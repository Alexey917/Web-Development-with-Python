from django.http import HttpResponse
import datetime


def index(request):
    current_year = datetime.date.today().strftime('%Y')
    start_date = datetime.date(int(current_year), 1, 1)
    end_date = start_date + datetime.timedelta(days=255)
    return HttpResponse(f'День программиста в этом году: {end_date}')

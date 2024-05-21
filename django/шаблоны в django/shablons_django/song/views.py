from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'song/index.html')


def french(request):
    return render(request, 'song/french.html')


def german(request):
    return render(request, 'song/german.html')


def spanish(request):
    return render(request, 'song/spanish.html')

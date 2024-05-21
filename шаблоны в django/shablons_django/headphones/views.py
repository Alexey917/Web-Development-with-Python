from django.shortcuts import render


# Create your views here.
def index(request):
    model = request.GET.get('model')
    if model == 'budslive':
        return render(request, 'headphones/samsung.html')
    elif model == 'airpods':
        return render(request, 'headphones/apple.html')
    else:
        return render(request, 'headphones/index.html')



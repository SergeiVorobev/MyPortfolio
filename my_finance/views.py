from django.shortcuts import render
from my_finance.models import MyApp


# Create your views here.
def home(request):
    # name = "John"
    all_apps = MyApp.objects.all()
    context = {
        'my_apps': all_apps
    }
    return render(request, 'website/index.html')

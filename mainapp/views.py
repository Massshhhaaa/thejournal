from django.shortcuts import render
from .models import Hello


# Create your views here.
def main_def(request):
    hello = Hello.objects.all()
    return render(request, 'mainapp/index.html', context={'hello' :hello})

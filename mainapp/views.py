from django.shortcuts import render


# Create your views here.
def main_def(request):
    return render(request, 'mainapp/index.html')
from django.shortcuts import render, get_object_or_404
from .models import Hello


# Create your views here.
def main_def(request):
    hello = Hello.objects.all()
    return render(request, 'mainapp/index.html', context={'hello' :hello})

def detail(request, slug):
    post = get_object_or_404(Hello, slug = slug)
    return render(request, "mainapp/post.html", {'post': post})

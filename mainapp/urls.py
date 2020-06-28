from django.urls import path
from .views import *


urlpatterns = [
    path('', main_def, name='main_def'),
]

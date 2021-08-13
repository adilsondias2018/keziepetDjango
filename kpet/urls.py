from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from kpet.views import AnimalView

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalView.as_view())

]

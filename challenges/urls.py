from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("", views.index),
    path("<int:month>", views.monthly_challenge_number),
    path("<str:month>", views.monthly_challenge)
]
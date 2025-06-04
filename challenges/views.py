from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn Django for atleast 20 minutes every day",
    "april": "Walk for atleast 20 minutes every day!",
    "may": "Learn Django for atleast 20 minutes every day",
    "june": "Eat no meat for the entire month",
    "july": "Walk for atleast 20 minutes every day!",
    "august": "Learn Django for atleast 20 minutes every day",
    "september": "Eat no meat for the entire month",
    "october": "Learn Django for atleast 20 minutes every day",
    "november": "Eat no meat for the entire month",
    "december": "Learn Django for atleast 20 minutes every day"
}

# Create your views here.
def january(request):
    return HttpResponse("January works! Eat no meat for the entire month")

def february(request):
    return HttpResponse("February works!")

def monthly_challenge_number(request, month):
    pass

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "Learn React for atleast 20 minutes every day",
    "april": "Walk for atleast 30 minutes every day!",
    "may": "Learn Django for atleast 20 minutes every day",
    "june": "Eat no meat for the entire month",
    "july": "Walk for atleast 20 minutes every day!",
    "august": "Learn Django for atleast 20 minutes every day",
    "september": "Eat no fries for the entire month",
    "october": "Learn FastAPI for atleast 20 minutes every day",
    "november": "Eat no meat for the entire month",
    "december": "Learn AWS for atleast 20 minutes every day"
}

# Create your views here.
def january(request):
    return HttpResponse("January works! Eat no meat for the entire month")

def february(request):
    return HttpResponse("February works!")

def monthly_challenge_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        forward_month = months[month - 1]
        # redirect_path = reverse("month-challenge", args=['january'])
        redirect_path = "/challenges/" + forward_month
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            'text': challenge_text,
            'month': month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = "/challenges/" + month
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        'months': months
    })

# def index(request):
#     render_to_string()
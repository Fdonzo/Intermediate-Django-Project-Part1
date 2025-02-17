# render does the same thing as django.template import render_to_string
#from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january"  : "Eat right for the entire month!" ,
    "february" : "Watch motivation lectures 20 minuates every day!",
    "march"    : "Learn Django for at least 20 minuates every day!",
    "april"    : "Learn Html for at least 20 minuates every day!",
    "may"      : "Learn Css for at least 20 minuates every day!",
    "june"     : "Learn SQl for at least 20 minuates every day!",
    "july"     : "Learn React for at least 20 minuates every day!",
    "august"   : "Learn Material UI for at least 20 minuates every day!",
    "september": "Learn internet and server for at least 20 minuates every day!",
    "october"  : "Learn gitHub for at least 20 minuates every day!",
    "november" : "Learn AWS for at least 20 minuates every day!",
    #"december" : "Learn ci/cd for at least 20 minuates every day!"
    "december" : None
}

def index(request):
  months = generate_list_of_months() 

  return render(request, "challenges/index.html", {
     "months": months
  })

def month_challenges_by_number(request, month):
   months = generate_list_of_months()
   if month > len(months):
      return HttpResponseNotFound("<h2>Invalid month</h2>")
   redirect_month = months[month-1]
   redirect_path  = reverse("month-challenge", args=[redirect_month])
   return HttpResponseRedirect(redirect_path)

def month_challenges(request, month):
   try:
       # render does the same thing as django.template import render_to_string
       #response_data = f"<h2>{challenge_text}</h2>"
       ##response_data = render_to_string("challenges/challenge.html")
       #return HttpResponse(response_data)
      #return render(request, render("challenges/challenge.html"))
      challenge_text = monthly_challenges[month]
      return render(request, "challenges/challenge.html", 
                    {"monthly_test": challenge_text,
                     "month_name": month
                     })
   
   except:
        raise Http404()
    
def generate_list_of_months():
   return list(monthly_challenges.keys())
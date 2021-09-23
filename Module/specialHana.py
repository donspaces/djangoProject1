from django.http import *
from django.shortcuts import *
import json

def specpage(request, luckynum, behaviour):
    context = dict()
    context["luck"] = luckynum
    context["behave"] = behaviour
    #context["display"] = json.dump(["Hana loves you too", "Stay with hana forever."])

    return render(request, "hanaluv.html", context)

def specgift(request, luckynum, behaviour):
    if request.POST:
        if(request.POST.get("code") == "hanailoveu"):
            return HttpResponseRedirect(reverse("secret"))

    return HttpResponseRedirect(reverse("hanapage", args=(luckynum,behaviour,)))

def secret(request):
    return render(request, "secret.html")
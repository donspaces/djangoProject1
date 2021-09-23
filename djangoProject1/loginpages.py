from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import *
import numpy as np

@login_required(login_url='/login/loginpage/')

def loginview(request):
    context = dict()
    context["user_profile"] = "profile: " + request.user.username

    context["luckynumber"] = np.random.randint(1, 30)
    context["behave"] = np.random.choice(["love me", "kiss me", "hug me", "talk to me", "cue me", "eat me", "be cute"])
    return render(request, "hrefs.html", context)

def logout(request):
    auth.logout(request)
    return redirect("/")

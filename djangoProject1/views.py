from django.http import HttpResponse
from django.shortcuts import *
import numpy as np

def sample(request):
    context = dict()
    context["user_profile"] = "profile"

    context["luckynumber"] = np.random.randint(1, 30)
    context["behave"] = np.random.choice(["love me", "kiss me", "hug me", "talk to me", "cue me", "eat me", "be cute"])

    context["status"] = "Log In"
    return render(request, "hrefs.html", context)

def search(request):
    context = dict()
    context["luckynumber"] = np.random.randint(1, 30)
    context["behave"] = np.random.choice(["love me", "kiss me", "hug me", "talk to me", "cue me", "eat me", "be cute"])

    try:
        if request.POST:
            return HttpResponseRedirect(reverse("Module:wiki", args=(request.POST["name"],)))
    except Exception as e:
        raise Http404("Sorry, the page you are trying to visit does not exist.")

    return render(request, "hrefs.html", context)

def testing_form(request):
    context = dict()
    context["text1"] = "This is a django webpage"
    context["text2"] = "The first django program made by Hanzhe Ye"
    context["link1"] = "<a href='https://www.baidu.com/s?ie=UTF-8&wd=febonacci%20series'>Febonacci Series</a>"

    return render(request, "sample.html", context)

def testing(request):
    context = dict()
    context["text1"] = "This is a django webpage"
    context["text2"] = "The first django program made by Hanzhe Ye"
    context["link1"] = "<a href='https://www.baidu.com/s?ie=UTF-8&wd=febonacci%20series'>Febonacci Series</a>"
    try:

        if "items" in request.POST:
            value = int(request.POST["items"])

        context["v"] = value

        assert value >= 0, "Invalid Number Error."
        assert value < 10001, "The number is too big."

        context["text3"] = [1, 1]
        for i in range(2, value):
            context["text3"].append(context["text3"][i - 1] + context["text3"][i - 2])

        context["text3"] = context["text3"][0:value]
    except Exception as e:
        context["warning"] = "Warning: " + e.args[0]
    finally:
        return render(request, "sample.html", context)
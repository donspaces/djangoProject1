from django.http import HttpResponse
from django.shortcuts import *

def math_form(request):
    context = dict()
    context["result"] = "0"
    context["oprends"] = ["+", "-", "*", "/", "%"]
    return render(request, "math.html", context)

def math(request):
    context = dict()
    context["oprends"] = ["+", "-", "*", "/", "%"]
    try:
        n1 = float(request.POST["factorI"])
        opr = str(request.POST["op"])
        n2 = float(request.POST["factorII"])

        context["value1"] = n1
        context["value2"] = n2

        if(opr == "+"):
            context["result"] = str(n1 + n2)
        elif (opr == "-"):
            context["result"] = str(n1 - n2)
        elif (opr == "*"):
            context["result"] = str(n1 * n2)
        elif (opr == "/"):
            context["result"] = str(n1 / n2)
        elif (opr == "%"):
            context["result"] = str(n1 % n2)

        context["oprends"].remove(opr)
        context["oprends"].insert(0,opr)

        return render(request, "math.html", context)
    except Exception as e:
        context["message"] = " Warning message: " + e.args[0]
        context["result"] = "NaN"
        return render(request, "math.html", context)


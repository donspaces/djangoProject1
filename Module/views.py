from django.http import *
from django.shortcuts import get_object_or_404, render
from .models import *
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "dbindex.html"
    context_object_name = "listitems"

    def get_queryset(self):
        return TableI.objects.order_by("name")[:50]

class DetailView(generic.DetailView):
    model = TableI
    template_name = "wikipage/wiki.xhtml"
    context_object_name = "TableI"

def dbtest(request):
    context = dict()
    context["disp"] = {"name": "", "birth": "", "height": ""}
    context["feedback"] = ""

    return render(request, "dbtest.html", context)

def commit(request):
    context = dict()
    try:
        if request.POST:
            name = request.POST["name"]
            birth = request.POST["birth"]
            height = request.POST["height"]

            if list(TableI.objects.filter(name=name)) != []:
                TableI.objects.filter(name=name).update(birth=birth, height=height)
            else:
                #insertion
                addlist = TableI(name=name, birth=birth, height=height)
                addlist.save()
    except Exception as e:
        context["warning"] = "Warning:" + e.args[0]
    else:
        context["feedback"] = "Successfully committed 1 line of data."

    return render(request, "dbtest.html", context)

def select(request):
    context = dict()
    try:
        if request.POST:
            key = request.POST["key"]
            result = get_object_or_404(TableI, name=key)
    except Exception as e:
        context["warning"] = "Warning:" + e.args[0]
    else:
        result.height = str(result.height) + " cm"
        context["disp"] = result
        context["feedback"] = "Successfuly display(ed) 1 line of data."

    return render(request, "dbtest.html", context)

def delete(request):
    context = dict()
    try:
        if request.POST:
            keydel = request.POST["keydel"]
            TableI.objects.get(name=keydel).delete()
    except Exception as e:
        context["warning"] = "Warning:" + e.args[0]
    else:
        context["feedback"] = "Successfuly delete(d) 1 line of data."

    return render(request, "dbtest.html", context)




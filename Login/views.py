from django.contrib import auth
from django.contrib.auth.models import User, AnonymousUser

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, SignupForm

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from .models import Pending

from urllib.parse import quote, unquote

# Create your views here.
def loginpage(request):
    context = dict()
    # login forms auto-generated
    context["function"] = "login"
    context["jump"] = {"link": reverse("Login:sign_up"), "text": "Join for the first time? Sign up."}
    if request.method == "GET":
        # created a form once the webpage opened
        form = LoginForm()
        context["form"] = form
        return render(request, "login/loginpage.html", context)
    else:
        # read the content from the form
        form = LoginForm(request.POST)
        context["form"] = form
        if form.is_valid(): # validating the form
            data = form.cleaned_data
            userSamp = auth.authenticate(username=data["username"], password=data["password"]) # Authentication
            if userSamp:
                # Authenticated sucessfully
                auth.login(request, userSamp)
                next = request.POST.get("next") or "/" # go to the next page
                return redirect(next)
            else:
                # unsuccessful
                context["error"] = "Username/Password Error: Forget password?" # print an error message
                return render(request, "login/loginpage.html", context)
        else:
            #formative errors (controlled by error_message properties)
            print(form.errors)
            # errors = form.errors.get("__all__")
            # context["error"] = errors
            return render(request, "login/loginpage.html", context)

def signuppage(request):
    context = dict()
    # sign up form
    context["function"] = "sign up"
    context["jump"] = {"link": reverse("Login:login"), "text": "Not a new user? Login."}
    if request.method == "GET":
        # create an empty form once open the page
        form = SignupForm()
        context["form"] = form
        return render(request, "login/loginpage.html", context)
    else:
        try:
            # read from the form
            form = SignupForm(request.POST)
            context["form"] = form
            if form.is_valid() and form.check(): # both validity and validation passed
                data = form.cleaned_data
                # avoid repetitions
                if(not User.objects.filter(username=data["username"]).exists()):
                    pendinfo = Pending(name=data["username"], passwd=data["password"], email=data["email"])
                    pendinfo.save() # upload user info into a pending table
                    return redirect(quote("/login/verifyemail/?name=" + data["username"])) # email validation
                else:
                    # repetitive
                    raise(Exception("The name you input has already been registered."))
            else:
                # formative form errors
                print(form.errors)

                raise(Exception("Registeration is invalid, please recheck your info"))
        except Exception as e:
                context["error"] = e.args[0] #all other exceptions captured
        # render
        return render(request, "login/loginpage.html", context)

def emailpage(request, username):
    # Http passed an encoded form of username information,
    # our task is to decode it to the normal format which
    # only consists string literals readable by computer.
    username = unquote(username) #decode (not decrypt)
    useremail = get_object_or_404(Pending, name=username).email
    # encoding to html
    subject = "Verification link[djangoProject1]"
    content = "Congratulations!\n" \
              "You have successfully created your account, now here is a link for verification:\n" \
              + "http://127.0.0.1:8000/login/verified" + quote("/?name=" + username + "/?code=" + useremail)

    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = useremail

    email = EmailMultiAlternatives(subject=subject, body=content, from_email=from_email, to=[to_email])
    email.send() # send an validation email to user

    return render(request, "login/emailpage.html", {email: useremail})

def verifypage(request, username, passcode):
    # userinfo validation (avoid non-registered users hacking)
    userinfo = get_object_or_404(Pending, name=unquote(username))
    # email validation with the passcode
    if userinfo.email == unquote(passcode):
        User.objects.create_user(username=userinfo.name, password=userinfo.passwd, email=userinfo.email)
        userinfo.delete() # clear pending account
        return render(request, "login/verysuccess.html")
    else:
        raise Http404(Exception("The page you are trying to find does not exist.")) # avoid domain-hack

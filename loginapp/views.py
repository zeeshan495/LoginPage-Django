from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import LoginForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm


def index_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home.html', {"username": username})
    else:
        context = {"tittle": "hello... it is home page"
                   }
        return render(request,"index.html",context)


def logout_page(request):
    try:
        logout(request)
        del request.session['username']
    except:
        pass
    # form = LoginForm(request.POST or None)
    # context = {"form": form}
    # return render(request, "login.html", context)

    return redirect("http://127.0.0.1:8000/login/")


def home_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        context = {"tittle": "hello... it is home page",
                   "username": username
                   }
        return render(request, 'home.html', context)
    else:
        form = LoginForm(request.POST or None)
        context = {"form": form}
        return render(request, "login.html", context)
    # if request.user.is_authenticated():
    #     context["premium"] = "you already logged in"
    # form = LoginForm(request.POST or None)
    # context = {"form": form}
    # return render(request,"login.html",context)


def login_page(request):
    print("inside login page")
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home.html', {"username": username})
    else:
        form = LoginForm(request.POST or None)
        context = {"form": form}
        print("inside login_page....inside else")
        # print(request.user.is_authenticated())
        if request.method == 'POST':
            form = LoginForm(request.POST)
            print("request post...inside first if")
            if form.is_valid():
                print("request post...inside second if")
                print(form.cleaned_data)
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    request.session['username'] = username
                    print(user)
                    login(request, user)
                    # Redirect to a success page.
                    # context['form'] = LoginForm()
                    return redirect("home")
                else:
                    # Return an 'invalid login' error message.
                    print("Error")
        return render(request, "login.html", context)

User = get_user_model()
def register_page(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'home.html', {"username": username})
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            new_user.is_staff = True
            new_user.is_superuser = True
            new_user.save()
            print(new_user)
            return redirect('login')
        # else:
            # form = UserCreationForm()
    return render(request, "register.html", context)

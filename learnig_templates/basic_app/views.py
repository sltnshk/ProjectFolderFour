from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
#from django.http import HttpResponseRidirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context_dict = {'text':"hello world","number":"100"}
    return render(request,'basic_app/index.html',context_dict)

@login_required
def special(request):
    return HttpResponse('you are logged in, Nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRidirect('index')

def other(request):
    return render(request,'basic_app/other.html')
def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password= password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRidirect(reverse('index'))
            else:
                return HttpResponse("Account not Active")

        else:
            print("Someone tried to login and failed")
            print("username:{} and password{}".format(username, password))
            return httpResponse("invalid login details supplied")
    else:
        return render(request, "basic_app/login.html",{})

from django.shortcuts import render
# from django.http import HttpResponse
from .forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

# Our original index view function
# corresponds to indexOLD.html (rename it to index.html to use it!)



def index(request):
    return render(request,'first_app/index_4.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            
            user = user_form.save()

            
            user.set_password(user.password)

            
            user.save()

            
            profile = profile_form.save(commit=False) 
            profile.user = user
            profile.save()

            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'first_app/register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
    


def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                print("Account Not Active!")
        else:
            return HttpResponse("invalid login details please go to login page and try again")
    
    else:
        return render(request,'first_app/login.html',{})
    


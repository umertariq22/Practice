from django.shortcuts import render
import datetime


# TODO: Create Signup View
def signup(request):
    day = [n for n in range(1,32) ]
    month = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
    now = datetime.datetime.now()
    year = [n for n in range(now.year,1905,-1)]
    return render(request, 'User/signup.html',context={'days':day,'months':month,'years':year})


# TODO:Create Login View
def login(request):
    return render(request,'User/signin.html')


# TODO: Create forgetPassword view


# TODO: Create Activate Account View


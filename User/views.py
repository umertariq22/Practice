import datetime
from django.shortcuts import render, redirect
from .models import User
from passlib.hash import pbkdf2_sha256
from articles import views


# TODO: Create Signup View
def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')
        if password == cpass:
            hashedPassword = pbkdf2_sha256.hash(password)
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')
        dob = str(date) + "-" + str(month) + "-" + str(year)
        user = User.objects.create(fname=fname, lname=lname, email=email, password=hashedPassword, dob=dob, gender=gender )
        if user.save():
            return redirect(views.main)
    day = [n for n in range(1, 32)]
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    now = datetime.datetime.now()
    year = [n for n in range(now.year, 1905, -1)]
    return render(request, 'User/signup.html', context={'days': day, 'months': month, 'years': year})


# TODO:Create Login View
def login(request):
    return render(request, 'User/signin.html')


# TODO: Create forgetPassword view


# TODO: Create Activate Account View

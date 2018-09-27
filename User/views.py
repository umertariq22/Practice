import datetime
from django.shortcuts import render


# TODO: Create Signup View
def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')
        gender = request.POST.get('gender')
        date = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')
        # print(fname, lname, email, password, cpass, gender, date, month, year)
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

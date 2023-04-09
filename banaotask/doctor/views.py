from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        pusername = request.POST['username']
        ppassword = request.POST['password']

        try:
            uid = User.objects.get(username=pusername)
        except User.DoesNotExist:
            # Display error message if the username doesn't exist
            error_message = 'Invalid username'
            return render(request, 'doctor/login.html', {'error_message': error_message})

        if uid.password == ppassword:
            if uid.role == "doctor":
                did = Doctor.objects.get(user_id=uid)
                request.session['email'] = uid.email  # session store
                context = {
                    'uid': uid,
                    'did': did,
                }
                return render(request, "doctor/doc-dashboard.html", context)

            elif uid.role == "patient":
                pid = Patient.objects.get(user_id=uid)
                request.session['email'] = uid.email  # session store
                context = {
                    'uid': uid,
                    'pid': pid,
                }
                return render(request, "patient/patient-dashboard.html", context)
        else:
            # Display error message if the password doesn't match
            error_message = 'Invalid password'
            return render(request, 'doctor/login.html', {'error_message': error_message})

    return render(request, 'doctor/login.html')


                        
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        role = request.POST.get('role')
        profile_pic = request.FILES.get('profilepic')

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'doctor/signup.html', {'emsg': 'Passwords do not match'})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'doctor/signup.html', {'emsg': 'Email is already registered'})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'doctor/signup.html', {'emsg': 'Username is already taken'})

        uid = User.objects.create(username=username, email=email, password=password, role=role)
        if role == 'doctor':
            did = Doctor.objects.create(user_id = uid, address=address, city=city, state=state, pincode=pincode, profile_pic=profile_pic,firstname=firstname,lastname=lastname, confirm_password=confirm_password)
            return redirect('login')
        elif role == 'patient':
            pid = Patient.objects.create(user_id=uid, address=address, city=city, state=state, pincode=pincode, profile_pic=profile_pic,firstname=firstname,lastname=lastname, confirm_password=confirm_password)
            return redirect('login')
        
    return render(request, 'doctor/signup.html')

            
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")


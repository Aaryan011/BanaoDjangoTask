from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.


def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect("login")
    else:
        return redirect("login")
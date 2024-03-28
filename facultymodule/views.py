from django.shortcuts import render

# Create your views here.
def facultypost(request):
    return render(request, 'facultymodule/facultypost.html')
from django.shortcuts import render

# Create your views here.
def viewexams(request):
    return render(request, 'studentmodule/viewexams.html')
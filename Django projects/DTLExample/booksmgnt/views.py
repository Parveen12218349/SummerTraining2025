from django.shortcuts import render

# Create your views here.
def book_list(request):
    books = [
        {"title": "C pmg", "author": "Gupta","available":False},
        {"title": "C++ pmg", "author": "Gupta ++","available":True},
        {"title": "Java pgm", "author": "Mohan","available":False},
        {"title": "python", "author": "Mohan", "available": False}
    ]
    return render(request,template_name='booksmgnt/base.html',context={'books':books})
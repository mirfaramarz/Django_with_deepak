from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'authentication/index.html')


def signUp(request):
    #return HttpResponse('signup')
    return render(request, 'authentication/signup.html')
    #import ipdb; ipdb.set_trace() # this is the debugger , line by line debugging
    

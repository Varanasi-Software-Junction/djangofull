from django.shortcuts import HttpResponse,render,redirect

def index(request):
    return HttpResponse('Home')
def showTemplate(request):
    return render(request,'hello.html')
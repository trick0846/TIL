from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'articles/index.html')

def myinfo(request):
    return render(request,'articles/myinfo.html')

def project(request):
    return render(request,'articles/project.html')

def skills(request):
    return render(request,'articles/skills.html')

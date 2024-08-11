from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def DS(request):
    return render(request,'DS.html')

def BC(request):
    return render(request,'BC.html')

def Bleach(request):
    return render(request,'Bleach.html')

def FT(request):
    return render(request,'FT.html')

def JJK(request):
    return render(request,'JJK.html')

def MHA(request):
    return render(request,'MHA.html')

def Naruto(request):
    return render(request,'naruto.html')

def OP(request):
    return render(request,'OP.html')

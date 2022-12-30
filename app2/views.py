from django.shortcuts import render

# Create your views here.
def user(request):
    d={'Name':'Atreya','Age':24,'Mobile':343344433}
    return render(request,'user.html',context=d) 
from django.shortcuts import render

# Create your views here.
def Jinja_print(request):
    d={'Name':'Atreya','Age':24}
    return render(request,'Jinja_print.html',context=d) 
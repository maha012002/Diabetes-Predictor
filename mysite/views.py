from django.http import HttpResponse
from django.shortcuts import render
import joblib

def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"Home.html")
def homecs(request):
    return render(request,"Home.css")
def result(request): 
    cls = joblib.load('final_model.sav')
    lis = []
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['pi'])
    
    print(lis)
    ans = cls.predict([lis])
    return render(request,"result.html",{'ans':ans})
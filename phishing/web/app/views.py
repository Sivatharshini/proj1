from django.shortcuts import render
from . ml import predict as pre

def predict(request):
    res = ""
    if request.method=='POST':
        url = request.POST['url']
        res = pre([url])
    return render(request,'index.html',{'url':res})
# Create your views here.

# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'f.html')
def capitalize(request):
    check=request.POST.get('removenum','off')
    check1=request.POST.get('removepunc', 'off')
    check2=request.POST.get('newlineremover', 'off')
    check3=request.POST.get('uppercase', 'off')
    djtext=request.POST.get('text', 'default')
    if check=="on":
        for char in  djtext:
            if (f"{char}").isalpha()==True:
                continue
            elif (f"{char}").isnumeric():
                djtext=djtext.replace(f"{char}","")
    if check1=="on":
        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        for char in  djtext:
            if char in punctuations:
                djtext = djtext.replace(f"{char}", "")
            else:
                continue
    if check2=="on":
        djtext=djtext.replace("\r","")
        djtext=djtext.replace("\n"," ")
    print(list(djtext))
    if check3=="on":
        djtext=djtext.upper()
    var={"dj_text":djtext}
    return render(request,"analyze.html",var)

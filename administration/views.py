from django.shortcuts import render
from . models import *

# Create your views here.
def admin_index(request):
    programs=program.objects.all()
    return render(request,'adminindex.html',{'program_list':programs})
def add(request):
    if request.method=="POST":
        program_no=request.POST.get('number')
        program_name=request.POST.get('name')
        discription = request.POST.get('desc')
        terms_condition = request.POST.get('termscondition')
        date = request.POST.get('date')
        venue = request.POST.get('venue')
        img = request.FILES['img']
        programdata=program(program_no=program_no,program_name=program_name,discription=discription,terms_condition=terms_condition,date=date,venue=venue,img=img)
        programdata.save()
    return render(request,'addprogram.html')
def details(request):
    programs=program.objects.get()
    return render(request,'adminmoredetails.html',{'programs':programs})

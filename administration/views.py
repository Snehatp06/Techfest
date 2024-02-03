from django.shortcuts import render,redirect
from . models import *
from .forms import programform
from django.http import HttpResponseRedirect
from django.urls import reverse

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
def details(request,id):
    programs=program.objects.get(program_no=id)
    return render(request,'adminmoredetails.html',{'programs':programs})
def update(request,id):
    programs=program.objects.get(program_no=id)
    form=programform(request.POST or None,request.FILES,instance=programs)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'programedit.html',{'form':form,'programs':programs})

def delete(request,id):
    if request.method=='POST':
        programs=program.objects.get(program_no=id)
        programs.delete()
        return redirect('/')
    return render(request,'programdelete.html')
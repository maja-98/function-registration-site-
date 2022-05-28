import os
from django.http import FileResponse, HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Member,Family
from django.db.models import Q
from .forms import *
from pathlib import Path
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.

def main(request):
    return render(request,'base/main.html')

def home(request,page):
    if request.method=='GET':
        fam = request.GET.get('fam') if request.GET.get('fam') else ''
        q = request.GET.get('q') if request.GET.get('q') else ''
        
        reg = [int(request.GET.get('reg'))] if request.GET.get('reg') else [0,1]

        members = Member.objects.filter(
            Q(family__family_name__icontains = fam) &
            Q(name__icontains = q) &
            Q(attended__in = reg)
        )
        
        total = len(members)
        member_per_page = 10
        pages = total//member_per_page+1 if total%member_per_page else total//member_per_page
        
        
        famForm= FamilyForm()
        families = Family.objects.all()
        
        if fam or q or reg !=[0,1]:
            filename = 'Export-filtered.csv'
        else:
            filename =  'Export-all.csv'
        with open(filename,'w') as file:
            print ('Name,Family,Age,Gender,participated',file=file)
            for member in members:
                print(member.name+','+member.family.family_name+','+str(member.age)+','+member.gender+','+str(member.attended),file=file)
        
        members = members [(page-1)*member_per_page:page*member_per_page]
        context={'members':members,'families':families,'famForm':famForm, 'range':range(1,pages+1)}
        return render(request,'base/index.html',context)
    if request.method=='POST':
        if request.POST.get('toggle',0):
            member = Member.objects.get(id= request.POST.get('toggle',0))
            member.attended = not member.attended
            member.save()
        
        if request.POST.get('family_name',''):
            family = Family.objects.create(family_name = request.POST.get('family_name'))
        
            
        
        return HttpResponseRedirect("#")
    

def editUser(request,id):
    member = Member.objects.get(id=id)
    form = MemberForm(instance=member)
    if request.method=='POST':
        form= MemberForm(request.POST ,request.FILES,instance=member)
        if form.is_valid():
            form.save()
        return redirect('home',1)
    context = {'member':member,'form':form}
    return render(request,'base/editUser.html',context)

def createUser(request):
    form = MemberForm()
    if request.method=='POST':
        form= MemberForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'User addedd Successfully')
        else:
            messages.error(request,'User is Not added')
        return redirect('create-user')
    context = {'form':form}
    return render(request,'base/createUser.html',context)

def download(request):
    print(os.listdir())
    files=list(filter(lambda x:x[::-1][:3]=='vsc',os.listdir()))
    files.sort(key=lambda x: os.path.getmtime(x))
    return FileResponse(open(files[-1],'rb'))

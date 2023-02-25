from django.shortcuts import render
from . models import About,Clients,ContactUs,Studio

def index(request):
    about=About.objects.filter().first()
    studio=Studio.objects.all().first()
    clients=Clients.objects.first()

    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        
        data=ContactUs.objects.create(
            fullname=fullname,
            email=email,
            subject=subject,
        )
        data.save()
    context={
        'about':about,
        'studio':studio,
        'clients':clients,
    }
    return render (request,'index.html',context)

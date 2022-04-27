from asyncio.windows_events import NULL
from django import views
from django.shortcuts import redirect, render
from .models import Case, Judge, Lawyer,Client
from login.views import un

# Create your views here.

'''def AdminDashboardAction(request):
    all_cases=Case.objects.all()
    all_lawyers=Lawyer.objects.all()
    all_judges=Judge.objects.all()
    all_clients=Client.objects.all()
    return render(request,'AdminDashboard.html', {'Cases': all_cases,'Lawyers': all_lawyers,'Judges':all_judges,'Clients':all_clients})

def RemoveJudgesAction(request):
    all_judges=Judge.objects.all()
    all_cases=Case.objects.all()
    return render(request,'RemoveJudges.html',{'Judges':all_judges,'Cases':all_cases})

def RemoveLawyersAction(request):
    all_lawyers=Lawyer.objects.all()
    all_cases=Case.objects.all()
    return render(request,'RemoveLawyers.html',{'Lawyers':all_lawyers,'Cases':all_cases})

def RemoveJudge(request,JudgeID):
    judge=Judge.objects.get(pk=JudgeID)
    judge.delete()
    return redirect('http://127.0.0.1:8000/RemoveJudges')

def RemoveLawyer(request,LawyerID):
    lawyer=Lawyer.objects.get(pk=LawyerID)
    lawyer.delete()
    return redirect('http://127.0.0.1:8000/RemoveLawyers')

def UpdateLawyer(request, LawyerID):
    lawyer=Lawyer.objects.get(pk=LawyerID)
    return render(request, 'UpdateLawyer.html',{'lawyer':lawyer})

#def LawyerDashboardAction(request):
    #lawyer=Lawyer.objects.get(pk=un)
    #return render(request,'LawyerDashboard.html',{'lawyer':lawyer})

def JudgeDashboardAction(request):

    return render(request,'JudgeDashboard.html')

def ClientDashboardAction(request):

    return render(request,'ClientDashboard.html')'''

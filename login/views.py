from asyncio.windows_events import NULL
from email.policy import default
import imp
from django.shortcuts import redirect, render
import mysql.connector as sql
from dashboard.models import Evidence, Lawyer,Judge,Client,Case
from django.db.models import Q
un=''
pwd=''
name=''
mno=0
exp=0
sr=0
city=''
street=''
pincode=0
age=0
caseid=0
casetype=''
caseinfo=''
dlem=''
plem=''
dcem=''
pcem=''
ver=''
evi=''
jem=''

# Create your views here.

def UserChoiceAction(request):
    return render(request,'UserChoice.html')

def LoginClientAction(request):

    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Password":
                pwd=value

        c="select * from dashboard_client where Email='{}' and Password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'LoginRetryClient.html')
        else:
            return redirect('http://127.0.0.1:8000/ClientDashboard')

    return render(request,'LoginClient.html')

def LoginJudgeAction(request):

    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Password":
                pwd=value

        c="select * from dashboard_judge where Email='{}' and Password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'LoginRetryJudge.html')
        else:
            return redirect('http://127.0.0.1:8000/JudgeDashboard')

    return render(request,'LoginJudge.html')

def LoginLawyerAction(request):

    global un,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Password":
                pwd=value

        c="select * from dashboard_lawyer where Email='{}' and Password='{}'".format(un,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'LoginRetryLawyer.html')
        else:
            return redirect('http://127.0.0.1:8000/LawyerDashboard',un)

    return render(request,'LoginLawyer.html')

def LoginAdminAction(request):

    global un,pwd
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="Username":
               un=value
            if key=="Password":
               pwd=value

        if (un=='admin@gmail.com' and pwd=='ADMIN') :
            return redirect('http://127.0.0.1:8000/AdminDashboard')
        else:
            return render(request,'LoginRetryAdmin.html')

    return render(request,'LoginAdmin.html')

def LawyerDashboardAction(request):
    lawyer=Lawyer.objects.filter(Q(Email=un))
    all_cases=Case.objects.filter(Q(ProsecutorLawyerEmail = un) | Q(DefenseLawyerEmail = un))
    all_clients=Client.objects.all()
    all_judges=Judge.objects.all()
    all_lawyers=Lawyer.objects.all()
    return render(request,'LawyerDashboard.html',{'lawyer':lawyer,'Cases':all_cases, 'Judges':all_judges,'Clients':all_clients,'Lawyers':all_lawyers})

def JudgeDashboardAction(request):
    judge=Judge.objects.filter(Q(Email=un))
    all_cases=Case.objects.filter(Q(JudgeEmail = un))
    all_clients=Client.objects.all()
    all_judges=Judge.objects.all()
    all_lawyers=Lawyer.objects.all()
    return render(request,'JudgeDashboard.html',{'judge':judge,'Cases':all_cases, 'Judges':all_judges,'Clients':all_clients,'Lawyers':all_lawyers})
    

def ClientDashboardAction(request):
    client=Client.objects.get(Q(Email=un))
    all_cases=Case.objects.filter(Q(DefenseClientEmail = un) | Q(ProsecutorClientEmail = un))
    all_clients=Client.objects.all()
    all_judges=Judge.objects.all()
    all_lawyers=Lawyer.objects.all()
    return render(request,'ClientDashboard.html',{'client': client,'Cases':all_cases, 'Judges':all_judges,'Clients':all_clients,'Lawyers':all_lawyers})

def AdminDashboardAction(request):
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

def UpdateLawyer(request):
    global un,name,mno,exp,pwd,sr

    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="WorkExperience":
                exp=value
            if key=="SuccessRate":
                sr=value

        if(pwd==cpwd):
            c="update dashboard_lawyer set Name='{}', ContactNo='{}', WorkExperience='{}', SuccessRate='{}',Password='{}' where Email='{}'".format(name,mno,exp,sr,pwd,un)
            cursor.execute(c)
            m.commit()
            return redirect('http://127.0.0.1:8000/LawyerDashboard')
    return render(request,'UpdateLawyer.html')


def UpdateJudge(request):
    global un,name,mno,exp,pwd,age

    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="YearsOfExp":
                exp=value
            if key=="Age":
                age=value

        if(pwd==cpwd):
            c="update dashboard_judge set Name='{}', Age='{}', ContactNo='{}', YearsOfExp='{}', Password='{}' where Email='{}'".format(name,age,mno,exp,pwd,un)
            cursor.execute(c)
            m.commit()
            return redirect('http://127.0.0.1:8000/JudgeDashboard')
    return render(request,'UpdateJudge.html')


def UpdateClient(request):
    global un,name,mno,exp,pwd,age

    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="Street":
                street=value
            if key=="City":
                city=value
            if key=="Pincode":
                pin=value

        if(pwd==cpwd):
            c="update dashboard_client set Name='{}', ContactNo='{}', City='{}', Street='{}', Pincode='{}', Password='{}' where Email='{}'".format(name,mno,city,street,pin,pwd,un)
            cursor.execute(c)
            m.commit()
            return redirect('http://127.0.0.1:8000/ClientDashboard')
    return render(request,'UpdateClient.html')

def FileCase(request):
    global caseid, casetype, caseinfo, dlem, plem, dcem, pcem

    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="CaseID":
                caseid=value
            if key=="CaseType":   
                casetype=value
            if key=="CaseInfo":
                caseinfo=value
            if key=="DefenseLawyerEmailID":
                dlem=value
            if key=="ProsecutorLawyerEmailID":
                plem=value
            if key=="DefenseClientEmailID":
                dcem=value
            if key=="ProsecutorClientEmailID":
                pcem=value
            if key=="JudgeEmailID":
                em=value
        c="insert into dashboard_case values('{}','{}','{}','','{}','{}','{}','{}','{}')".format(caseid,casetype,caseinfo,dlem,plem,em,dcem,pcem)
        cursor.execute(c)
        m.commit()
        return redirect('http://127.0.0.1:8000/LawyerDashboard')
    return render(request,'FileCase.html')


def GiveVerdict(request,Caseid):
    global ver
    case=Case.objects.get(Q(CaseID=Caseid))
    all_lawyers=Lawyer.objects.all()
    all_clients=Client.objects.all()
    all_evidence=Evidence.objects.filter(Q(CaseID=Caseid))
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Verdict":
                ver=value
        c="update dashboard_case set Verdict='{}' where CaseID='{}'".format(ver,Caseid)
        cursor.execute(c)
        m.commit()
        return redirect('http://127.0.0.1:8000/JudgeDashboard')
    return render(request,'Verdict.html',{'case':case, 'Lawyers': all_lawyers, 'Clients':all_clients, 'CaseNo':Caseid,'Evidence':all_evidence})


def SubmitEvidence(request,Caseid):
    global evi
    case=Case.objects.get(Q(CaseID=Caseid))
    em=case.JudgeEmail
    all_lawyers=Lawyer.objects.all()
    all_clients=Client.objects.all()
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Evidence":
                evi=value
        c="insert into dashboard_evidence values('{}','{}','{}')".format(Caseid,evi,un)
        cursor.execute(c)
        m.commit()
        return redirect('http://127.0.0.1:8000/LawyerDashboard')
    return render(request,'Evidence.html',{'case':case, 'Lawyers': all_lawyers, 'Clients':all_clients, 'CaseNo':Caseid})


def UpdateCase(request,Caseid):
    case=Case.objects.get(Q(CaseID=Caseid))

    global caseid, casetype, caseinfo, dlem, plem, dcem, pcem

    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="CaseType":   
                casetype=value
            if key=="CaseInfo":
                caseinfo=value
            if key=="DefenseLawyerEmailID":
                dlem=value
            if key=="ProsecutorLawyerEmailID":
                plem=value
            if key=="DefenseClientEmailID":
                dcem=value
            if key=="ProsecutorClientEmailID":
                pcem=value
            if key=="JudgeEmailID":
                jem=value
        c="update dashboard_case set CaseType='{}',CaseInfo='{}' where CaseID='{}'".format(casetype,caseinfo,Caseid)
        cursor.execute(c)
        m.commit()
        Case.objects.filter(pk=Caseid).update(DefenseLawyerEmail=dlem)
        Case.objects.filter(pk=Caseid).update(ProsecutorLawyerEmail=plem)
        Case.objects.filter(pk=Caseid).update(DefenseClientEmail=dcem)
        Case.objects.filter(pk=Caseid).update(ProsecutorClientEmail=pcem)
        Case.objects.filter(pk=Caseid).update(JudgeEmail=jem)
        return redirect('http://127.0.0.1:8000/LawyerDashboard')
    return render(request,'UpdateCase.html',{'Case':case})
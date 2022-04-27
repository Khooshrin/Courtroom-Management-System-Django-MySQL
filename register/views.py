from django.shortcuts import render
import mysql.connector as sql
name=''
em=''
mno=0
city=''
street=''
pin=0
pwd=''
cpwd=''
age=0
exp=0
dep=''
sr=0
ld=''

# Create your views here.

def RegisterClientAction(request):

    global name,em,mno,city,street,pin,pwd,cpwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="Email":
                em=value
            if key=="ContactNo":   
                mno=value
            if key=="City":
                city=value
            if key=="Street":
                street=value
            if key=="Pincode":
                pin=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="DepName":
                dep=value

        if(pwd==cpwd):
            c="insert into dashboard_client values('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,em,mno,city,street,pin,pwd,1)
            cursor.execute(c)
            m.commit()
            c="insert into dashboard_client_dependent values('{}','{}')".format(em,dep)
            cursor.execute(c)
            m.commit()
            return render(request,'ClientDashboard.html')
        else :
            return render(request,'RegisterRetryClient.html')

    return render(request,'RegisterClient.html')

def RegisterJudgeAction(request):

    global un,name,age,em,mno,exp,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="Email":
                em=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="Age":
                age=value
            if key=="YearsOfExp":
                exp=value

        if(pwd==cpwd):
            c="insert into dashboard_judge values('{}','{}','{}','{}','{}','{}')".format(name,age,em,mno,exp,pwd)
            cursor.execute(c)
            m.commit()
            return render(request,'JudgeDashboard.html')
        else :
            return render(request,'RegisterRetryJudge.html')          

    return render(request,'RegisterJudge.html')  

def RegisterLawyerAction(request):

    global un,name,age,em,mno,exp,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Project2OOPs!",database='courtroom_system')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="Email":
                em=value
            if key=="ContactNo":   
                mno=value
            if key=="Password":
                pwd=value
            if key=="ConfPassword":
                cpwd=value
            if key=="Age":
                age=value
            if key=="WorkExperience":
                exp=value
            if key=="SuccessRate":
                sr=value
            if key=="LawDomain":
                ld=value

        if(pwd==cpwd):
            c="insert into dashboard_lawyer values('{}','{}','{}','{}','{}','{}')".format(name,em,mno,exp,sr,pwd)
            cursor.execute(c)
            m.commit()
            c="insert into dashboard_lawyer_domain values('{}','{}')".format(ld,em)
            cursor.execute(c)
            m.commit()
            return render(request,'LawyerDashboard.html')
        else :
            return render(request,'RegisterRetryLawyer.html')

    return render(request,'RegisterLawyer.html')
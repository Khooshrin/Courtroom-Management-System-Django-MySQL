from asyncio.windows_events import NULL
from operator import mod
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Lawyer(models.Model):
    Name=models.CharField(max_length=45)
    Email=models.EmailField(primary_key=True)
    ContactNo=models.IntegerField()
    WorkExperience=models.IntegerField()
    SuccessRate=models.IntegerField()
    Password=models.CharField(max_length=20)

class Lawyer_Domain(models.Model):
    LawyerEmail=models.ForeignKey(Lawyer,on_delete=models.CASCADE,primary_key=True,db_constraint=False)
    Domain=models.CharField(max_length=45)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['LawyerEmail','Domain'],name='domain_lawyer') ]

class Judge(models.Model):
    Name=models.CharField(max_length=45)
    Age=models.IntegerField()
    Email=models.EmailField(primary_key=True)
    ContactNo=models.IntegerField()
    YearsOfExp=models.IntegerField()
    Password=models.CharField(max_length=20)

class Client(models.Model):
    Name=models.CharField(max_length=45)
    Email=models.EmailField(primary_key=True)
    ContactNo=models.IntegerField()
    City=models.CharField(max_length=45)
    Street=models.CharField(max_length=45)
    Pincode=models.IntegerField()
    LawyerEmail=models.ForeignKey(Lawyer,on_delete=models.CASCADE,db_constraint=False)
    Password=models.CharField(max_length=20)

class Client_Dependent(models.Model):
    ClientEmail=models.ForeignKey(Client,on_delete=models.CASCADE,primary_key=True,db_constraint=False)
    DependentName=models.CharField(max_length=45)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['ClientEmail','DependentName'],name='dependent_client') ]

class Case(models.Model):
    CaseID=models.IntegerField(primary_key=True,auto_created=True)
    CaseType=models.CharField(max_length=45)
    DefenseLawyerEmail=models.ForeignKey(Lawyer,on_delete=models.CASCADE,related_name='DefenseLawyer',db_constraint=False)
    ProsecutorLawyerEmail=models.ForeignKey(Lawyer,on_delete=models.CASCADE,related_name='ProsecutorLawyer',db_constraint=False)
    DefenseClientEmail=models.ForeignKey(Client,on_delete=models.CASCADE,related_name='DefenseClient',db_constraint=False,default=NULL)
    ProsecutorClientEmail=models.ForeignKey(Client,on_delete=models.CASCADE,related_name='ProsecutorClient',db_constraint=False,default=NULL)
    CaseInfo=models.CharField(max_length=45)
    JudgeEmail=models.ForeignKey(Judge,on_delete=models.CASCADE,db_constraint=False,default=NULL,null=True)
    Verdict=models.CharField(max_length=45,null=True,default=NULL)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['DefenseLawyerEmail','ProsecutorLawyerEmail'],name='two_diff_lawyers') ] 

class Evidence(models.Model):
    CaseID=models.ForeignKey(Case,on_delete=models.CASCADE,primary_key=True)
    LawyerEmail=models.ForeignKey(Lawyer,on_delete=models.CASCADE)
    EvidenceInfo=models.CharField(max_length=100)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['CaseID','LawyerEmail'],name='evidence_lawyer_case') ]







    
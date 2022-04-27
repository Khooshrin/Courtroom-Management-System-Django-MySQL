"""CourtroomManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from login.views import UpdateCase, SubmitEvidence,GiveVerdict,FileCase, UpdateClient, UpdateJudge,LoginClientAction, UpdateLawyer, UserChoiceAction, LoginLawyerAction, LoginJudgeAction, LoginAdminAction, LawyerDashboardAction, AdminDashboardAction, ClientDashboardAction, JudgeDashboardAction, RemoveJudgesAction, RemoveLawyersAction, RemoveJudge, RemoveLawyer
from register.views import RegisterClientAction, RegisterJudgeAction, RegisterLawyerAction
#from dashboard.views import AdminDashboardAction, ClientDashboardAction, JudgeDashboardAction, RemoveJudgesAction, RemoveLawyersAction, RemoveJudge, RemoveLawyer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',UserChoiceAction),
    path('LoginAdmin',LoginAdminAction),
    path('LoginAdmin#',LoginAdminAction),
    path('LoginClient',LoginClientAction),
    path('LoginJudge',LoginJudgeAction),
    path('LoginLawyer',LoginLawyerAction),
    path('LoginClient#',LoginClientAction),
    path('LoginJudge#',LoginJudgeAction),
    path('LoginLawyer#',LoginLawyerAction),
    path('RegisterClient/',RegisterClientAction),
    path('RegisterJudge/',RegisterJudgeAction),
    path('RegisterLawyer/',RegisterLawyerAction),
    path('RegisterClient/#',RegisterClientAction),
    path('RegisterJudge/#',RegisterJudgeAction),
    path('RegisterLawyer/#',RegisterLawyerAction),
    path('RegisterClient/#',RegisterClientAction),
    path('RegisterJudge/#',RegisterJudgeAction),
    path('RegisterLawyer/#',RegisterLawyerAction),
    path('AdminDashboard',AdminDashboardAction),
    path('ClientDashboard',ClientDashboardAction),
    path('LawyerDashboard',LawyerDashboardAction),
    path('JudgeDashboard',JudgeDashboardAction),
    path('RemoveJudges',RemoveJudgesAction),
    path('RemoveLawyers',RemoveLawyersAction),
    path('RemoveJudge/<JudgeID>',RemoveJudge, name='delete-judge'),
    path('RemoveLawyer/<LawyerID>',RemoveLawyer, name='delete-lawyer'),
    path('UpdateLawyer',UpdateLawyer),
    path('UpdateJudge',UpdateJudge),
    path('UpdateClient',UpdateClient),
    path('FileCase',FileCase),
    path('GiveVerdict/<Caseid>',GiveVerdict,name='give-verdict'),
    path('SubmitEvidence/<Caseid>',SubmitEvidence,name='submit-evidence'),
    path('EditCase/<Caseid>',UpdateCase,name='edit-case'),
]

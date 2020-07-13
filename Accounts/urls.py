from django.urls import path
from . import views
urlpatterns = [
    path("loginPage",views.loginPage,name="loginPage"),
    path("registerPage",views.registerPage,name="registerPage"),
    path("homepage",views.homePage,name="homePage"),
    path("",views.index,name="index"),
    path("workerDash",views.workerDash,name="workerDash"),
    path("workerProfile",views.workerProfile,name="workerProfile"),
    path("workerPlist",views.workerPlist,name="workerPlist"),
    path("workerAppt",views.workerAppt,name="workerAppt"),
    path("logoutpage",views.logout_page,name="logoutpage"),
 
    
]
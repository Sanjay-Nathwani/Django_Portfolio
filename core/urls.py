from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.aboutPage,name="about"),
    path('contact/',views.contactPage,name="contact"),
    path('project/<str:pk>/',views.projectPage,name="project"),
    path('add-project/',views.addProject,name="add-project"),
    path('edit-project/<str:pk>/',views.editProject,name="edit-project"),
    path('delete-project/<str:pk>/',views.deleteProject,name="delete-project"),
    path('inbox/',views.inboxPage,name="inbox"),
    path('message/<str:pk>/',views.messagePage,name="message"),
    path('add-skill/',views.addSkill,name="add-skill"),
    path('add-endorsement/',views.addEndorsement,name="add-endorsement"),
    path('payment/',views.payment,name="payment"),
    path('payment-status/',views.payment_status,name="payment-status"),
    path('chart/',views.chartPage,name="chart"), 


    path('login/',views.loginPage,name="login"),   
    path('signup/',views.signupPage,name="signup"),   
    path('logout/',views.logoutPage,name="logout"),   
]

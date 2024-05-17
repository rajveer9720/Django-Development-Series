

from django.urls import path
from . import views

urlpatterns = [
    
    path("student/", views.studentinfo, name="Student"),
    path("userinfo/", views.userinfo, name="userinfo"),
    path("success/", views.thankyou, name="success"),
    

    

    
   
    

]

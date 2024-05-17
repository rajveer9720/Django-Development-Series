from django.contrib import admin
from django.urls import include, path
from myWebSite import views


urlpatterns = [
  
    path('admin/', admin.site.urls),
    
    path('',include('myWebSite.urls')),
  

]
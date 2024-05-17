from django.shortcuts import render
from django.http import HttpResponseRedirect

from myWebSite.models import Student
from .forms import usermessege

# if need any forms fields go on any browser search built it fieldsS
def thankyou(request):
   return render(request,'myWebSite/success.html')

  
def userinfo(request):
  if request.method =='POST':

    fm = usermessege(request.POST)
    if fm.is_valid():
      print('Form validated')
      name = fm.cleaned_data['name']
      roll_no = fm.cleaned_data['roll_no']
      agree = fm.cleaned_data['agree']
      price = fm.cleaned_data['price']
      
   
      print('Name:-', name)
      print('Roll no:-',roll_no)
      print('Agree:-',agree)
      print('PRICE:-',price)
  
      return HttpResponseRedirect('/success/')
    
  else:
    fm = usermessege()
    # fm.order_fields (field_order=['email','name','subject','desc'])
  
  return render(request,'myWebSite/userinfo.html',{'form':fm})

    
def studentinfo(request):
    stud = Student.objects.all()
    print('myoutput',stud)
    return render (request, 'myWebSite/student.html',{'stu' :stud})
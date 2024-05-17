from django import forms

class usermessege(forms.Form):
    name = forms.CharField(label='Enter Your Name',label_suffix='-', min_length=5, max_length=20,empty_value='aryan', error_messages=({'required':'Enetr your Name'}) ) 
    roll_no =forms.IntegerField(min_value=1,max_value=500)
    price =forms.DecimalField (min_value=1,max_value=500)
    agree = forms.BooleanField(label= 'I agree')
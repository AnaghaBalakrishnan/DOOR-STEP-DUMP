from django import forms
from .models import Booking









class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        widgets={
            'number_of_bags':forms.NumberInput(attrs={"class":"form-control","type":"number","placeholder":"Number of bags"}),
            'cname':forms.TextInput(attrs={"class":"form-control","placeholder":"Full Name"}),
            'address':forms.TextInput(attrs={"class":"form-control","min":1,"placeholder":"Address"}),
            'house_no':forms.NumberInput(attrs={"class":"form-control","min":1,"placeholder":"House Number"}),
            # 'type':forms.Select(attrs={"class":"form-control","placeholder":"Waste Category"}),
            'ph':forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter the available date"}),
            'date':forms.DateInput(attrs={"class":"form-control","placeholder":"Name in the Card","type":"date"}),
            'cardname':forms.NumberInput(attrs={"class":"form-control","placeholder":"Card Number (1111-2222-3333-4444)"}),
            'cardnumber':forms.NumberInput(attrs={"class":"form-control","placeholder":"Exp Date(00/0000)"}),
            'exp':forms.NumberInput(attrs={"class":"form-control","placeholder":"Phone Number"}),
            'cvv':forms.NumberInput(attrs={"class":"form-control","placeholder":"CVV (111)"}),
        }


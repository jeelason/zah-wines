from django import forms
from wines.models import Contact 


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

# class ConsultForm(forms.ModelForm):
#     class Meta:
#         model = Consultant
#         fields = "__all__"
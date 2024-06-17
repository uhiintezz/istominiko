from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['created_at']
        widgets = {
           'name': forms.TextInput(attrs={'class': "form-control footer-input margin-b-20", 'name':"name", 'id':"name", 'type':"text", 'placeholder':"Имя"}),
           'email': forms.EmailInput(attrs={'class': "form-control footer-input margin-b-20", 'name':"email", 'id':"email", 'type':"email", 'placeholder':"почта"}),
           'phone': forms.TextInput(attrs={'class': "form-control footer-input margin-b-20", 'name':"phone", 'id':"phone", 'type':"text", 'placeholder':"телефон"}),
           'message': forms.Textarea(attrs={'class': "form-control footer-input margin-b-30", 'name':"name", 'id':"name", 'type':"text", 'placeholder':"Ваше сообщение", 'rows':"6"})
        }

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Enter Your Name')
    email = forms.EmailField(label='Enter Email Address')
    subject = forms.CharField(max_length=150, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Enter Your Message')
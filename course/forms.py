from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'special', 'size': '40'}))
    #message = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50}))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

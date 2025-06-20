from django import forms
from .models import SupportTicket, TicketReply

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['name', 'email', 'message', 'attachment']

    # Optional: Add custom widget for better file input styling
    def __init__(self, *args, **kwargs):
        super(SupportTicketForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5})
        self.fields['attachment'].widget.attrs.update({'class': 'form-control'})

class TicketReplyForm(forms.ModelForm):
    class Meta:
        model = TicketReply
        fields = ['message']

class ContactSupportForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            'required': True,
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'required': True,
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Your Message',
            'rows': 5,
            'required': True,
        })
    )

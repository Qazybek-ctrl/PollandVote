from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from .models import Poll

class PollCreateForm(ModelForm):
    class Meta:
        model = Poll
        fields = [
            'title',
            'description',
            'option1',
            'option2',
            'option3'
        ]

        widgets = {
            'title' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"title", 
                'placeholder':"Title of your new poll"
            }),
            'description' : Textarea(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"description", 
                'placeholder':"Enter your description here"
            }),
            'option1' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"option1", 
                'placeholder':"Option 1"
            }),
            'option2' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"option2", 
                'placeholder':"Option 2"
            }),
            'option3' : TextInput(attrs={
                'class':"input100", 
                'type':"text", 
                'name':"option3", 
                'placeholder':"Option 3"
            })
        }
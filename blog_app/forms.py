from django import forms
from .models import Posts


class TopicForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = '__all__'
        labels = {'desc':'Descripiton'}
        widgets = {
            'topic':forms.TextInput(attrs={
                'class':'form-control',
                
            }),
            'desc':forms.Textarea(attrs={
                'class':'form-control'
            }),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'

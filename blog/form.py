from django import forms
from .models import Blog
    # class Meta:
    #     model = Blog
    #     fields = ['title', 'body']
class BlogPost(forms.ModelForm)
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','one'), ('2','two'),('3','three')])

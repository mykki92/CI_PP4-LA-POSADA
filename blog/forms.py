from .models import Comment
from django import forms


# Comment form for the blog page
class BlogComments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

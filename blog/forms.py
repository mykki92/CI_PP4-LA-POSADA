from .models import Comment
from django import forms


# Comment form for the blog page
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

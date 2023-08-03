from django import forms
from .models import BlogPost, Comments


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text',]
        
from django import forms
from .models import Comment,Blog
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['body',]


class CreatePostForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields =['title', 'image', 'description','category','publish']
        widget = {'description':CKEditorWidget}
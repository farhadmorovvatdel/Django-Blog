from django import forms
from django.core.validators import MinValueValidator

from .models import Comment,Blog
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['body']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields =['title', 'image', 'description','category','publish']


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','publish','description','category','image',]

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class RatePostForm(forms.Form):
    rate=forms.IntegerField(min_value=0,max_value=5)


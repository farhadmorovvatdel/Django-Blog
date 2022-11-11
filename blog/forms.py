from django import forms
from django.core.validators import MinValueValidator

from .models import Comment,Blog



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['body']


class CreatePostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
         super(CreatePostForm, self).__init__(*args, **kwargs)
         self.fields['title'].required = True
         self.fields['category'].required = True

    class Meta:
        model =Blog
        fields =['title', 'image', 'description','category','publish']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'image': forms.FileInput(attrs={'class': 'form-control'}),
        # 'description': forms.CharField(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),

     }
        error_messages={
            'title':{
                'required':'this field is required'
            },
            'category':{
                'required':'this field is required'
            }
        }




class UpdatePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdatePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['category'].required = True

    class Meta:
        model = Blog
        fields = ['title', 'image', 'description', 'category', 'publish']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            # 'description': forms.CharField(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }



class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class RatePostForm(forms.Form):
    rate=forms.IntegerField(min_value=0,max_value=5)



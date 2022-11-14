from unicodedata import category

from django import forms
from django.core.validators import MinValueValidator

from .models import Comment, Blog, RatePost


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].required =True
        self.fields['body'].label ='comment'
    class Meta:
        model = Comment
        fields=['body',]
        widgets = {
            'body':forms.Textarea(attrs={'cols':30,'rows':10 }),
        }



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


class RatePostForm(forms.ModelForm):
    rate = forms.IntegerField(min_value=0,max_value=5)
    def __init__(self, *args, **kwargs):
        super(RatePostForm, self).__init__(*args, **kwargs)
        self.fields['rate'].required = True

    class Meta:
        model = RatePost
        fields = ['rate',]






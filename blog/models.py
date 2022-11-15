from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import  slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Avg



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'


class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_blog')
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.BooleanField(default=False)
    image=models.ImageField(upload_to='blogs/',blank=True)
    description=RichTextUploadingField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',null=True)
    likes=models.ManyToManyField(User,related_name='userlike',)
    unlikes=models.ManyToManyField(User,related_name='userunlike')
    def __str__(self):
        return  f'{self.user.username}-{self.title}'

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        return super(Blog, self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'

    def LikePost(self):
        return reverse('blog:LikePost',args={self.id})
    def UnLikePost(self):
        return reverse('blog:UnLikePost',args={self.id})
    def TotalLikes(self):
        total=self.likes.count()
        return total
    def TotalUnLikes(self):
        total=self.unlikes.count()
        return total

    def AddComment(self):
        return reverse('blog:AddComment',args={self.id})

    def get_absolute_url(self):
        return reverse('blog:detail',args={self.id})

    def TotalComments(self):
        total=self.postcomment.count()
        return total

    def AvragePostRate(self):
        rate=self.postrate.aggregate(Avg('rate'))
        if (rate['rate__avg']) is None:
             return 'there is no rate'
        else:
            return str(round(rate['rate__avg'],2))
    def TotalCountRate(self):
        total=self.postrate.count()
        return total

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usercomment',null=True)
    post= models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='postcomment',null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'

    def DeleteComment(self):
        return reverse('blog:DeleteComment',args={self.id})
    def UpdateComment(self):
        return reverse('blog:UpdateComment',args={self.id})




class RatePost(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='rateuser',null=True)
    post= models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='postrate')
    rate = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], null=True, blank=True)



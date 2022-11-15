from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from accounts.models import Profile
from .models import Blog, Comment, RatePost
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import CommentForm,CreatePostForm,UpdatePostForm,RatePostForm,UpdateCommentForm
from .mixins import UserLoginMixin,UserAccessMixin
from .decorator import UserLoginRequired,UserAccess




class All_Blogs(ListView):
    context_object_name = 'blog'
    template_name = 'blog/allblogs.html'
    paginate_by = 3

    def get_queryset(self):
        blog=Blog.objects.filter(publish=True)
        return  blog



class DetailPost(DetailView):
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    model=Blog

    def get_object(self,**kwargs):
        pk=self.kwargs['pk']
        queryset = get_object_or_404(Blog,pk=pk)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(DetailPost, self).get_context_data(**kwargs)
        context['commentform']=CommentForm
        context['addrateform']=RatePostForm

        return context





class CreatePost(LoginRequiredMixin,CreateView):
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:user_post')
    form_class = CreatePostForm

    def form_valid(self,form):
        print(self.request.path)
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(CreatePost, self).form_valid(form)
    def get_context_data(self):
        context = super(CreatePost, self).get_context_data()
        context["profile"]=Profile.objects.get(user=self.request.user)
        return context




class UserPost(UserLoginMixin,View):
    def get(self,request):
        posts=Blog.objects.filter(user=self.request.user)
        profile=get_object_or_404(Profile,user=self.request.user)
        return render(request,'blog/userblogs.html',{'posts':posts,'profile':profile})




class UpdatePost(UserLoginMixin,UserAccessMixin,UpdateView):
    model = Blog
    success_url = reverse_lazy('blog:user_post')
    template_name = 'blog/upatepost.html'
    form_class =UpdatePostForm
    def get_object(self,queryset=None):
        pk=self.kwargs['pk']
        query=Blog.objects.get(pk=pk)
        return query
    def get_context_data(self, **kwargs):
        context=super(UpdatePost, self).get_context_data(**kwargs)
        context['profile']=Profile.objects.get(user=self.request.user)
        return context



class DeletePost(LoginRequiredMixin,UserAccessMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:user_post')
    template_name ='blog/confirm_delete.html'

    def get_object(self,queryset=None):
        pk=self.kwargs['pk']
        query=Blog.objects.get(pk=pk)
        return query
    def get_context_data(self, **kwargs):
        context=super(DeletePost, self).get_context_data(**kwargs)
        context['profile']=Profile.objects.get(user=self.request.user)
        return context



@UserLoginRequired()

def AddComment(request,id):
    post=get_object_or_404(Blog,id=id)
    user=request.user
    commentform=CommentForm(request.POST or None)
    if commentform.is_valid():
        body=commentform.cleaned_data['body']
        newcomment=commentform.save(commit=False)
        newcomment.user=user
        newcomment.post=post
        newcomment.body=body
        newcomment.save()
        return redirect('blog:detail',post.id)
    return render(request,'blog/detail.html')

@UserLoginRequired()
@UserAccess()
def DeleteComment(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('blog:detail',comment.post.id)


@UserLoginRequired()
@UserAccess()
def UpdateComment(request,comment_id):
    commentt=get_object_or_404(Comment,id=comment_id)
    updatecomment = UpdateCommentForm(request.POST or None,instance=commentt)
    if updatecomment.is_valid():
       body = updatecomment.cleaned_data['body']
       comment = Comment.objects.filter(id=comment_id).update(body=body)
       return redirect('blog:detail',commentt.post.id)
    return render(request,'blog/updatecomment.html',{'updatecomment':updatecomment,'comment_id':comment_id})

@UserLoginRequired()
def AddRate(request,post_id):
    post=get_object_or_404(Blog,pk=post_id)
    form=RatePostForm(request.POST or None)
    is_exists=RatePost.objects.filter(user=request.user, post=post).exists()
    if is_exists:
        messages.error(request,'you alreday sent rate','danger')
        return redirect ('blog:detail',post.id)
    rateform=form.save(commit=False)
    rateform.post=post
    rateform.user=request.user
    rateform.rate=form.cleaned_data['rate']
    rateform.save()
    return redirect('blog:detail',post.id)

@UserLoginRequired()
def AddLikePost(request,id):
    post=get_object_or_404(Blog,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    post.unlikes.remove(request.user)
    messages.success(request,'you like this post','success')
    return redirect('blog:detail',post.id)

@UserLoginRequired()
def AddUnlikePost(request,id):
    post=get_object_or_404(Blog,id=request.POST.get('post_id'))
    post.unlikes.add(request.user)
    post.likes.remove(request.user)
    messages.success(request, 'you unlike this post', 'success')
    return redirect('blog:detail', post.id)





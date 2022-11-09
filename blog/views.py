from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404
from django.views import View

from .models import Blog
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView

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
    model = Blog


class CreatePost(LoginRequiredMixin,CreateView):
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('blog:Blogs')
    model = Blog
    fields = ['title','image','description']

    def form_valid(self,form):
        print(self.request.path)
        obj=form.save(commit=False)
        obj.user=self.request.user
        return super(CreatePost, self).form_valid(form)



class UserPost(View):
    def get(self,request):
        posts=Blog.objects.filter(user=self.request.user)
        return render(request,'blog/userblogs.html',{'posts':posts})

class DeletePost(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:user_post')
    template_name ='blog/confirm_delete.html'
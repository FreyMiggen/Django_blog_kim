from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.core.files.storage import FileSystemStorage
from .models import Post
from .forms import PostForm
from authentication.decorators import unauthenticated_user
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.
def home_view(request):
    return render(request,'myblog/home.html',{})

class Blog_Post(ListView):
    model=Post
    template_name='myblog/blog_post.html'

def detail_post(request,post_id):
    liked=False
    post=Post.objects.get(id=post_id)
    total_likes=post.total_likes()
    likes=Post.objects.get(id=post_id).likes.all()
    if post.likes.filter(id=request.user.id).exists():
        liked=True
    else:
        liked=False

    return render(request,'myblog/detail_post.html',{'post':post,'total_likes':total_likes,'likes':likes,'liked':liked})

def post_form(request):
    submitted=False
    kim=User.objects.get(id=request.user.id)
    if request.method=='POST':
        
        form=PostForm(request.POST,request.FILES,initial={'author':kim})
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect('postform?submitted=True')
    else:
        form=PostForm(initial={'author':kim})
        if 'submitted' in request.GET:
            submitted=True
    
    
    
    return render(request,'myblog/post_form.html',{'form':form,'submitted': submitted,'kim':kim})

# def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.author = self.request.user
#         self.object.save()
#         return super().form_valid(form)

def like_view(request,post_id):
    liked=False
    post=Post.objects.get(id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
    #post=get_object_or_404(Post,id=request.POST.get("post_id"))# to determine whether the button Like gets submitted by referring to the button Like by its name
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('detail-post', args=[str(post_id)]))

def upload_file(request):
    if request.method=='POST':
        uploaded_file=request.FILES.get('document')
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        name=fs.save(uploaded_file.name,uploaded_file)
        url=fs.url(name)

        # print(uploaded_file.name)
        # print(uploaded_file.size)

    return render(request,'myblog/upload_file.html',{'url':url})


def update_post(request,post_id):
    
    post=Post.objects.get(pk=post_id)
    form=PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog-post')
    return render(request,'myblog/update_post.html',{'form':form,'post':post})


def delete_post(request,post_id):
    post=Post.objects.get(pk=post_id)
    if request.method=='POST':

        post.delete()
    
        return  redirect('blog-post')
        
    return render(request,'myblog/delete_post.html',{'post':post})





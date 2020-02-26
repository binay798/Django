from django.shortcuts import render,redirect
from .models import Posts
from .forms import TopicForm,EditForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    posts = Posts.objects.order_by('-date')
    popular = Posts.objects.order_by('-date')[:3]
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    topics = Posts.objects.order_by('-date')[:2]
    try:
        items = paginator.page(page)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        items = paginator.page(1)
    
    context = {'items':items,'popular':popular,'topics':topics}
    return render(request,'blog.html',context)


def add_post(request):
    if request.method == 'POST':
        form = TopicForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("valid")
            return redirect('/')
        else:
            print("not valid")
    else:
        print(request.method)
        form = TopicForm()
        context = {'form':form}
        return render(request,'New_post_form.html',context)


def edit_post(request,post_id):
    post = Posts.objects.get(id=post_id)
    if request.method == 'POST':
        form = EditForm(instance=post,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditForm(instance=post)
        context = {'form':form,'post':post}
        return render(request,'edit_form.html',context)
    
def delete(request,post_id):
    post = Posts.objects.get(id=post_id)
    post.delete()
    return redirect('/')
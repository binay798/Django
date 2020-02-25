from django.shortcuts import render,redirect
from .models import Posts
from .forms import TopicForm
# Create your views here.
def index(request):
    posts = Posts.objects.order_by('-date')
    popular = Posts.objects.order_by('-date')[:3]
    topics = Posts.objects.order_by('-date')
    context = {'posts':posts,'popular':popular,'topics':topics}
    return render(request,'blog.html',context)

def add_post(request):
    if request.method == 'POST':
        form = TopicForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('/')
    form = TopicForm()
    context = {'form':form}
    return render(request,'form.html',context)

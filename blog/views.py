from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.



def home(request):
    allposts="deepak"

    allposts=Post.objects.all()


    context={'allposts':allposts}

    return render(request,'blog/bloghome.html',context)




def post(request,slug):
    return render(request,'blog/blogpost.html')



def db(request):
    return render(request,'blog/db.html')
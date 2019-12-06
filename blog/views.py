from django.shortcuts import render,HttpResponse

# Create your views here.



def home(request):

    return render(request,'blog/bloghome.html')


def post(request,slug):
    return render(request,'blog/blogpost.html')



def db(request):
    return render(request,'blog/db.html')
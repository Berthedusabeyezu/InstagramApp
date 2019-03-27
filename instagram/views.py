from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm,NewImageForm,NewCommentForm,LikeForm
from .models import Profile,Image,Comment,Like
from django.contrib.auth.models import User
# Create your views here.

def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune')
    profile = Profile.objects.all()
    image = Image.objects.all()
    return render(request, 'welcome.html',{"image":image})
def search_profiles(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = profile.search_by_bio(search_term)
        message = f"{search_term}"

        return render(request, 'all-profile/search.html',{"message":message,"profiles": searched_profiles})
      
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-profile/search.html',{"message":message})
def profile(request,id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user = user)
   
    # profile = Profile.objects.all()
    return render(request, 'profile.html',{"one":profile})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()   
        return redirect('new-profile')
    
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def images(request):
    image = Image.objects.all()
    return render(request, 'welcome.html',{"image":image})

def image(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect("welcome")

    else:
        form = NewImageForm()
    return render(request, 'image.html', {"form": form})

@login_required(login_url='/accounts/login/')
def cmt(request,image_id):
    image = Image.objects.get(id = image_id)
    comment = Comment.objects.filter(image = image.id).all() 
    likes = Like.objects.filter(image = image.id).all() 

    return render(request,'cmt.html',{"image":image,"comment":comment,"likes":likes})

def comment(request,image_id):
    current_user = request.user
    image = Image.objects.get(id = image_id)
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image=image
            comment.save()
        return redirect('welcome')

    else:
        form = NewCommentForm()
    return render(request, 'comment.html', {"form": form,'image':image})


def likes(request,image_id):
    current_user = request.user
    image = Image.objects.get(id = image_id)
    if request.method == 'POST':
        form = LikeForm(request.POST, request.FILES)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = current_user
            likes.save()
        return redirect('welcome')

    else:
        form = LikeForm()
    return render(request, 'likes.html', {"form": form,'image':image})

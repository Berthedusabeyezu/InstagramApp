from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm,NewImageForm,NewCommentForm,LikeForm
from .models import Profile,Image,Comment,Like
# Create your views here.

def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune')
    profile = Profile.objects.all()
    return render(request, 'welcome.html',{"profile":profile})
def search_profiles(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = profile.search_by_bio(search_term)
        message = f"{search_term}"

        return render(request, 'all-profile/search.html',{"message":message,"profiles": searched_profiles})
      
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-profile/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form
            profile.image = current_user
            profile.save()
        return redirect('welcome')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def images(request):
    image = Image.objects.all()
    return render(request, 'images.html',{"image":image})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('Images')

    else:
        form = NewImageForm()
    return render(request, 'image.html', {"form": form})

def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('comment')

    else:
        form = NewCommentForm()
    return render(request, 'comment.html', {"form": form})

def likes(request):
    current_user = request.user
    if request.method == 'POST':
        form = LikeForm(request.POST, request.FILES)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = current_user
            likes.save()
        return redirect('likes')

    else:
        form = LikeForm()
    return render(request, 'likes.html', {"form": form})

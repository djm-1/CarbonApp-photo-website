from django.shortcuts import render,HttpResponseRedirect
from .forms import UserProfileForm,UserPostForm
from .models import UserProfile,PicturePost


#homepage
def home(request):
    return render(request,'home.html')


# user profile update system
def index(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except:
            profile = UserProfile.objects.create(user=request.user)
        form=UserProfileForm(instance=profile)
        if request.method == "POST":
            form=UserProfileForm(request.POST,request.FILES,instance=profile)
            # print(form.is_valid())
            # print(form.cleaned_data)
            if form.is_valid():
                profile.delete()
                form.save()
                return HttpResponseRedirect('/profile/')
        else:
            return render(request,'signup.html',{'form':UserProfileForm})
    else:
        return render(request,'signup.html')


# making post
# authenticateed users can make a post...but un-authenticated users can only view all posts
def make_post(request):
    all_posts=PicturePost.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            # form=UserPostForm(request.POST,request.FILES)
            # if form.is_valid():
            new_post=PicturePost(author=request.user,post_pic=request.FILES['post_pic'],
                    post_topic=request.POST['post_topic'])
            new_post.save()
            return HttpResponseRedirect('/posts/')
        else:
            return render(request,'makepost.html',{'form':UserPostForm,'posts':all_posts})
    else:
        return render(request,'makepost.html',{'posts':all_posts})



# delete post : authenticated user can only delete own post
def delete_post(request,post_id):
    if request.user.is_authenticated:
        posts=PicturePost.objects.get(id=post_id)
        posts.delete()
        return HttpResponseRedirect('/posts/')


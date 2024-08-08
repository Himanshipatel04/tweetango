from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from .models import Tweet
from .forms import TweetForm
# Create your views here.
def index(request):
   return render(request,'index.html')

def tweet_list(request):
   tweets = Tweet.objects.all().order_by('-created_at')
   return render(request,'tweet_list.html',{'tweets':tweets})

def create_tweet(request):
   if request.method == "POST":
      form = TweetForm(request.POST,request.FILES)
      if form.is_valid:
         tweet = form.save(commit=False)
         tweet.user = request.user
         tweet.save()
         return redirect('tweet_list')
   else:
      form = TweetForm()
   return render(request,"tweet_form.html",{'form':form})

def edit_form(request,tweet_id):
     tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user) #(model,pk)
     if request.method == "POST":
       form = TweetForm(request.POST,request.FILES,instance=Tweet)
       if form.is_valid:
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('tweet_list')
     else:
        form = TweetForm(instance=tweet)
     return render(request,"tweet_form.html",{'form':form})



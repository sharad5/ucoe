from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Post_Highlight

def post_list(request):
	posts = Post.objects.all()
	posth = Post_Highlight.objects.all()
	
	return render(request, 'notice/post_list.html', {'posth': posth})
	return render(request, 'notice/post_list.html', {'posts': posts})




	
    


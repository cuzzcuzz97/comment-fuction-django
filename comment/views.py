from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment, Post, Reply
from .forms import CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.



def postDetail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    comments = Comment.objects.filter(post=post)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

    return render(request, 'comment/post-detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


def commentList(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)

    return render(request, 'comment/comment-list.html', {
        'comments': comments,
        # 'form': CommentForm()
    })

def commentCreate(request):
    form = CommentForm()
    context = {
        'form' : form
    }
    return render(request, 'comment/comment-create.html',context)
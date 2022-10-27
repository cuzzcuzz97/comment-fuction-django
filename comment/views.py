from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment, Post, Reply
from .forms import CommentForm, ReplyForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.


def postDetail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    comments = Comment.objects.filter(post=post)
    
    formcomment = CommentForm(request.POST or None)
    replyform = ReplyForm(request.POST or None)

    if request.method == "POST":
        target_id = request.POST.get("target"," ")
        if formcomment.is_valid():
            comment = formcomment.save(commit=False)
            comment.post = post
            if request.user.is_authenticated:
                comment.username = request.user.username
            comment.save()
        if replyform.is_valid():
            try:
                target = Comment.objects.get(id=target_id)
                reply = replyform.save(commit=False)
                reply.target = target
                reply.save()
                # reply.save()
                # print(reply)
                # reply.target = Comment.objects.get(id=)
            except:
                ...
                
    return render(request, 'comment/post-detail.html', {
        'post': post,
        'comments': comments,
        'formcomment': formcomment,
        'replyform': replyform,
    })


def commentList(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post)

    return render(request, 'comment/comment-list.html', {
        'comments': comments,
        'form': CommentForm()
    })

def commentCreate(request):
    form = CommentForm()
    
    context = {
        'formcomment' : form
    }
    return render(request, 'comment/comment-create.html',context)

def replyCreate(request, id):
    form = ReplyForm()
    target_id = id
    context = {
        'replyform' : form,
        'target_id' : target_id
    }
    return render(request, 'comment/reply-create.html', context)

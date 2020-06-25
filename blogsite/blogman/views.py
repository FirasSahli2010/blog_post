# from django.shortcuts import render
#
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Blog
from .models import Comment

from .forms import *

from django.core.paginator import Paginator

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    blog_list = Blog.objects.order_by('-pub_date')

    post_page_counter = Paginator(blog_list, 5) # Show 5 posts per page.

    page_number = request.GET.get('page')
    page_obj = post_page_counter.get_page(page_number)

    context = {'blog_list': blog_list, 'page_obj': page_obj}


    return render(request, 'blog/index.html', context)


def detail(request, blog_id):
    try:
        post = Blog.objects.get(pk=blog_id)
        postComments = Comment.objects.filter(blog_id=blog_id)

        postComment_page_counter = Paginator(postComments, 5) # Show 5 contacts per page.

        page_number = request.GET.get('page')
        page_obj = postComment_page_counter.get_page(page_number)

        context = {'post': post, 'page_obj': page_obj}

    except Blog.DoesNotExist:
        raise Http404("Post is not available")
    except Comment.DoesNotExist:
        postComments = []

    commentForm = CommentForm()

    context = {'post': post, 'postComments': postComments, 'commentForm':commentForm}
    return  render(request, 'blog/details.html', context)

def addcomment(request, blog_id):
    commentBody = request.POST['comment_text']
    visitor_name =  request.POST['visitor_name_text']
    blog = get_object_or_404(Blog, pk= blog_id)
    post_id = blog_id
    comment = Comment(blog_id = blog, commentText= commentBody, visitor_name = visitor_name )
    comment.save()

    try:
        post = Blog.objects.get(pk=blog_id)
        postComments = Comment.objects.filter(blog_id=post)
        postComment_page_counter = Paginator(postComments, 5) # Show 5 contacts per page.

        page_number = request.GET.get('page')
        page_obj = postComment_page_counter.get_page(page_number)

    except Blog.DoesNotExist:
        raise Http404("Post is not available")
    except Comment.DoesNotExist:
        postComments = []

    commentForm = CommentForm()

    context = {'post': post, 'postComments': postComments, 'commentForm':commentForm, 'page_obj': page_obj}
    return  render(request, 'blog/details.html', context)

def results(request, blog_id):
    response = "You're looking at the results of blog %s."
    # return HttpResponse(response % blog_id)

def comment (request, blog_id):
    return HttpResponse("You're voting on blog %s." % blog_id)

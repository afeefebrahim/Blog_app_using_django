from django.shortcuts import render
from blog_app.forms import postForm,userForm,userprofileForm,commentForm
from blog_app.models import blog_post,Comment
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def index(request):
	post_list = blog_post.objects.order_by('-heading')
	context_dict = {'post': post_list}
	return render(request,'blog_app/index.html',context_dict)
def post_data(request):
	if request.method == 'POST':
	    form = postForm(request.POST)
	    if form.is_valid():
	        form.save(commit = True)
	        return index(request)

	    else:
	        print form.errors
	else:
	    form = postForm

	return render(request, 'blog_app/post.html', {'form': form})   
import json

def post_details(request,post_head_slug):
    context_dict = {}
    if request.method == 'POST':
      comment_in  = request.POST.get('comment',None)
      p = blog_post.objects.get(slug=post_head_slug)
      Comment.objects.create(post = p,comment = comment_in)
      c = Comment.object.filter(post = p)
      a = []
      for k in c:
          a.append(k.Comment)
      f = json.dumps({'json':a})     
      return HttpResponse(f) 
    try:
       Post = blog_post.objects.get(slug = post_head_slug)
       print "post is",Post       
       context_dict['heading'] = Post.heading
       context_dict['blog_p'] = Post
       context_dict['text'] = Post.text 
       commends = Comment.objects.filter(post=Post)
       print "hell0"
       print commends
       context_dict['commends'] = commends
       print "comments = ", context_dict['commends'] 
    except blog_post.DoesNotExist:
       print "helloblog"
       print post_head_slug	
       pass 

    return render(request,'blog_app/post_detail.html',context_dict)   

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = userForm(data=request.POST)
        profile_form = userprofileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors,profile_form.errors

    else:
        user_form = userForm()
        profile_form = userprofileForm
    return render (request,'blog_app/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user:
            if user.is_active:
               login (request,user)
               return HttpResponseRedirect('/blog_app/')
            else:
               return HttpResponse("your account is disable")
        else:
             print "Invalid login details: {0}, {1}".format(username, password)
             return HttpResponse("Invalid login details supplied.")   
    else:        
       return render(request,'blog_app/login.html',{}) 
@login_required       
def user_logout(request):
     logout(request)
     return HttpResponseRedirect('/blog_app/')

def edit(request):
    post_list = blog_post.objects.order_by('-heading')
    context_dict = {'post': post_list}
    return render(request,'blog_app/edit.html',context_dict)

def edited_post(request,post_head_slug):
    context_dict = {}
    if request.method == 'POST':
        print "helloblog" 
        heading_in  = request.POST.get('head',None)
        text_msg_in = request.POST.get('post_msg',None)
        print heading_in
        print text_msg_in
        p = blog_post.objects.get(slug=post_head_slug)
        p.heading = heading_in
        p.text = text_msg_in
        p.save()    
        #HttpResponseRedirect('/blog_app/')
        return redirect(index)   

    try:
       Post = blog_post.objects.get(slug = post_head_slug)    
       context_dict['blog_p'] = Post
    except blog_post.DoesNotExist: 
       pass 

    return render(request,'blog_app/edited_post.html',context_dict)

def delete_post(request,post_head_slug):
     blog_post.objects.get(slug=post_head_slug).delete()
     return redirect(index)
         


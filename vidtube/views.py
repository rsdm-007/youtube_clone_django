from django.shortcuts import render,redirect,get_object_or_404
#from .forms import barform
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from .models import account,post,subcribe,view,User,like,comment
from django.contrib.auth import get_user,authenticate,login,logout,views
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import QuerySet,Q
from random import Random,shuffle
from django.urls import reverse
import json
import logging
@login_required(login_url='../login/')
def my_view(request):
    #message = "Hello, this is a message from the view!"
    posts=post.objects.all()
    user1=account.objects.get(user=request.user)
    if posts is None:
        return render(request,'home.html',{'user1':user1})
    return render(request,'home.html',{'posts':posts,'user1':user1,'title':"VidTube"})
def signup(request):
    if request.method=='POST':
        username= request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password2']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username")
                return render(request,"signup.html") 
                #return HttpResponse("username")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email")
                return render(request,"signup.html")          
            else:
                user=User.objects.create(username=username,email=email)
                user.set_password(password)
                user.save()
                #U_model=account.get(id=User.id)
                new_user=User.objects.get(username=username)
                new_model=account.objects.create(user=new_user,id_user=new_user.id)
                new_model.save()
                return HttpResponseRedirect('../login/')
        else:
            #messages.info(request,"password mismatch")
            messages.info(request,"password mismatch")
            return render(request,"signup.html")
            #return HttpResponse("")            
    else:
        return render(request,"signup.html")
def signup1(request):

    if request.method=='POST':
        username= request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return HttpResponse("email")
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return HttpResponse("username")
            else:
                user = User.objects.create(username=username, email=email,)
                user.set_password(password)
                user.save()
                user_model=User.objects.get(username=username)
                new=account.objects.create(user=user_model,id_user=user_model.id)
                new.save()
                return HttpResponseRedirect('../login/')
                

        else:
            messages.info(request,'Password not matching')
            return redirect('../signup/')    

    return render(request,'signup.html')
def login_view(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('../home/')
        else:
            return HttpResponse("Invalid")
        
    return render(request,'login.html')
@login_required(login_url='../login/')
def search(request):
    user1=account.objects.get(user=request.user)
    if request.method=='GET':
        key=request.GET['SearchInput']
        posts=post.objects.filter(Q(des__icontains=key)|Q(user__user__username__icontains=key))

        return render(request,'search.html',{'posts':posts,'title':key,'user1':user1})
    return render(request,'search.html',)
@login_required(login_url='../login/')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('../login/')
    
@login_required(login_url='../login/')
def upload(request):
    if request.method=="POST":
        thumb=request.FILES.get('Thumbnail')
        des=request.POST['des']
        user1=account.objects.get(user=request.user)
        if thumb:
            new=post.objects.create(thumb=thumb,des=des,user=user1)
        else:
            new=post.objects.create(des=des,user=user1)
        new.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,'upload.html',)
def setting(request):
    if request.method=="POST":
        img=request.FILES.get('profileid')
        u_model=account.objects.get(user=request.user)
        if img:
            u_model.dp=img
            u_model.save()
            return HttpResponseRedirect("../home/")
        else:
            return HttpResponse("../settings/")
    else:
        return render(request,"settings.html")
def watch(request):
    watch=request.GET.get('watch')
    vid=post.objects.get(id=watch)
    posts=post.objects.all().exclude(id=watch)
    user1=account.objects.get(user=request.user)
    comments=comment.objects.filter(vid_id=vid.id)
    username=request.user.username
    if posts is None:
        return render(request,'home.html',{'user1':user1})
    #return render(request,'home.html',{'title':"VidTube"})
    if  view.objects.filter(vid_id=watch,user=username).first() is None:
        new=view.objects.create(vid_id=watch,user=username)
        new.save()
        vid.views+=1
        vid.save()
    if subcribe.objects.filter(acc_id=vid.user.id_user,user=username).first(): 
       flag=True
        #return HttpResponse('unsubcribed')
        
    else:
        flag=False
    return render(request,"watch.html",{'post':vid,'posts':posts,'user1':user1,'flag':flag,'comments':comments})
def subs(request):
    username=request.user.username
    acc_id=request.GET.get('acc_id')
    acc=account.objects.get(id_user=acc_id)
    if subcribe.objects.filter(acc_id=acc_id,user=username).first(): 
        mod1=subcribe.objects.filter(acc_id=acc_id,user=username)
        mod1.delete()
        acc.subscribers-=1
        #return HttpRespoe('unsubcribed')
        
    else:
        new=subcribe.objects.create(acc_id=acc_id,user=username)
        new.save()
        print('saved')
        acc.subscribers+=1
        #return HttpResponse('subcribed')
    acc.save()
    referrer_url = request.META.get('HTTP_REFERER')
    return redirect(referrer_url)
def likes(request):
    username=request.user.username
    acc_id=request.GET.get('acc_id')
    acc=post.objects.get(id=acc_id)
    if like.objects.filter(acc_id=acc_id,user=username).first(): 
        mod1=like.objects.filter(acc_id=acc_id,user=username)
        mod1.delete()
        acc.likes-=1
        #return HttpRespoe('unsubcribed')
        
        
    else:
        new=like.objects.create(acc_id=acc_id,user=username)
        new.save()
        print('saved')
        acc.likes+=1
        #return HttpResponse('subcribed')
    acc.save()
    referrer_url = request.META.get('HTTP_REFERER')
    return redirect(referrer_url)
def channel(request,key):
    username=request.user.username
    user1=account.objects.get(user=request.user)
    #channel_id=request.GET.get('channel_id')
    #channel_user=User.objects.filter(username=key)
    channel=get_object_or_404(account,user__username=key)
    #acc=account.objects.get(id_user=channel_id)
    #return HttpResponse(channel.dp,content_type='image/png')
    if subcribe.objects.filter(acc_id=channel.id_user,user=username).first(): 
       flag=True
        #return HttpResponse('unsubcribed')
        
    else:
        flag=False
    posts=post.objects.filter(user=channel)
    return render(request,"channek.html",{'user1':user1,'channel':channel,'flag':flag,'posts':posts})
    #return render(request,'channek.html',)
# def comment(request):
#     username=request.user.username
#     acc_id=request.GET.get('acc_id')
#     acc=account.objects.get(id_user=acc_id)
#     if subcribe.objects.filter(acc_id=acc_id,user=username).first(): 
#         mod1=subcribe.objects.filter(acc_id=acc_id,user=username)
#         mod1.delete()
#         acc.subscribers-=1
#         #return HttpRespoe('unsubcribed')
        
#     else:
#         new=subcribe.objects.create(acc_id=acc_id,user=username)
#         new.save()
#         print('saved')
#         acc.subscribers+=1
#         #return HttpResponse('subcribed')
#     acc.save()
#     referrer_url = request.META.get('HTTP_REFERER')
#     return redirect(referrer_url)
# logger = logging.getLogger(__name__)
def comment_view(request):
    try:
        data = json.loads(request.body)
        comment_text = data.get('comment', '')
        acc_id = request.GET.get('acc_id')
        user1=account.objects.get(user=request.user)
        # logger.info(f'comment_view called with data: acc_id={acc_id}, username={username}, comment={comment_text}')
        # Ensure all necessary data is present
        if acc_id and comment_text and user1:
            new_comment = comment.objects.create(vid_id=acc_id, user=user1, comments=comment_text)
            new_comment.save()
            return JsonResponse({'success': True, 'message': 'Comment submitted successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Missing required data'})

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    
    # Redirect to referrer URL on GET requests or if POST request was unsuccessful
   

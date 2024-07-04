"""
URL configuration for youtube_clone_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from vidtube.views import my_view,signup,login_view,search,upload,logout_view,setting,watch,subs,channel,likes,comment_view
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',my_view,name='home'),
    #path('create/',create),
    path('upload/',upload),
    path('signup/',signup),
    path('login/',login_view),
    path('search/',search),
    path('logout/',logout_view),
    path('settings/',setting),
    path('subcribe/',subs,name='acc_id'),
    path('watch',watch,name='watch'),
    path('like/',likes,name='acc_id'),
    path('@<str:key>',channel,name='channel_id'),
    path('comment/',comment_view,name='acc_id')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
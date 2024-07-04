from django.contrib import admin
from django.contrib.auth.models import User
from .models import account,post,subcribe,view,like,comment
admin.site.register(account)
admin.site.register(post)
admin.site.register(subcribe)
admin.site.register(view)
admin.site.register(like)
admin.site.register(comment)
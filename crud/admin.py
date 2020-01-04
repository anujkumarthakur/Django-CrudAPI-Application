from django.contrib import admin

#add this to import the Post model
from .models import Post
#add this to register the Post model
admin.site.register(Post)


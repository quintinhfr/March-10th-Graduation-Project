from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# Creation of Initial Data Models

#Profile

admin.site.register(Profile)

#-------------------------------------------------------------------------------------------------

#Post

admin.site.register(Post)

#-------------------------------------------------------------------------------------------------

#Post Liking

admin.site.register(LikePost)

#-------------------------------------------------------------------------------------------------

#Followers

admin.site.register(FollowersCount)

#-------------------------------------------------------------------------------------------------
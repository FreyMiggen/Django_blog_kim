from django.urls import path
from .views import detail_post, home_view,Blog_Post, post_form, update_post, upload_file,delete_post,like_view







urlpatterns = [
    path('',home_view,name='home'),
    path('blogpost/',Blog_Post.as_view(),name='blog-post'),
    path('detailpost/<int:post_id>/',detail_post,name='detail-post'),
    path('postform',post_form,name='post-form'),
    path('uploadfile',upload_file,name='upload-file'),
    path('updatepost/<int:post_id>/',update_post,name='update-post'),
    path('deletepost/<int:post_id>/',delete_post,name='delete-post'),
    path('like/<int:post_id>/',like_view,name='post-likes'),
]
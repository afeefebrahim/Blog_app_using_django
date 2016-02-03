from django.conf.urls import  url
from blog_app import views
urlpatterns = [
    url(r'^blog_post/$',views.post_data ,name = "post"),
    url(r'^$',views.index,name="index"),
    url(r'^blog_post/(?P<post_head_slug>[\w\-]+)/$',views.post_details,name = 'post_details'),
    url(r'^register/$',views.register,name='register'), 
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'), 
    url(r'^edit/$',views.edit,name = 'edit'),
    url(r'^edit/(?P<post_head_slug>[\w\-]+)/$',views.edited_post,name = 'post_edited'),
    url(r'^delete/(?P<post_head_slug>[\w\-]+)/$',views.delete_post,name = 'post_delete'),
]
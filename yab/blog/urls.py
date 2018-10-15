from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/edit/(?P<pk>[0-9]+)/$', views.post_edit, name="post_edit"),
    url(r'^post/drafts/$', views.post_draft, name="post_draft_list"),
    url(r'^post/publish/(?P<pk>[0-9]+)/$', views.post_publish, name="post_publish"),
    url(r'^post/del/(?P<pk>[0-9]+)/$', views.post_remove, name="post_remove"),
    url(r'^post/add_comment_to_post/(?P<pk>[0-9]+)/$', views.add_comment_to_post, name="add_comment_to_post"),
    url(r'^comment/approve/(?P<pk>[0-9]+)/$', views.comment_approve, name="comment_approve"),
    url(r'^comment/remove/(?P<pk>[0-9]+)/$', views.comment_remove, name="comment_remove"),
   
]
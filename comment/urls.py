from django.urls import path
from .views import (
    postDetail,
    commentList,
    commentCreate,
    replyCreate
)

urlpatterns = [
    path('<slug>/', postDetail, name='post-detail'),
    path('<slug>/comment', commentList, name='comment-list'),
    path('comment/create',commentCreate , name='comment-create'),
    path('comment/<id>/reply',replyCreate , name='reply-create'),

]
from django.urls import path
from .views import (
    postDetail,
    commentList,
    commentCreate
)

urlpatterns = [
    path('<slug>/', postDetail, name='post-detail'),
    path('<slug>/comment', commentList, name='comment-list'),
    path('comment/create',commentCreate , name='comment-create'),

]
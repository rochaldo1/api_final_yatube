from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet,
                    FollowViewSet,
                    GroupViewSet,
                    PostViewSet)

router = DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('v1/', include(router.urls)),
]

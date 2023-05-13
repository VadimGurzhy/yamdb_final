from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, TokenObtainView,
                    UserRegistrationView, UserViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet, )
router.register('categories', CategoryViewSet, )
router.register('genres', GenreViewSet, )
router.register('titles', TitleViewSet, )
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path(
        'v1/auth/signup/',
        UserRegistrationView.as_view(),
        name='signup',
    ),
    path(
        'v1/auth/token/',
        TokenObtainView.as_view(),
        name='get_token',
    ),
    path('v1/', include(router.urls)),
]

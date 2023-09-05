from .views import LoginView, SignUpView, LogoutView, UserAPIView
from .views import PostViewSet
from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet


router = routers.DefaultRouter()
router.register("Comment", CommentViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('profile/', UserAPIView.as_view(), name="profile"),
    path('signup/', SignUpView.as_view(), name='token-signup'),
    path('login/', LoginView.as_view(), name='token-login'),
    path('logout/', LogoutView.as_view(), name='token-logout'),
]

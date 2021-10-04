from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (
    PostListView,
    PostDetailView, PostOptionView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SignUpView,
    GratitudePostListView, QuestionPostListView,
    UserPostSave, UserPostHide, PostOptionEdit,
    SavePostListView, HidePostListView,
)
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # landing page
    path('', views.landing, name='home'),

    # list views
    path('posts/', PostListView.as_view(), name='post-list'),
    path('gratitude/', GratitudePostListView.as_view(), name='post-gratitude'),
    path('question/', QuestionPostListView.as_view(), name='post-gratitude'),
    path('saved/', SavePostListView.as_view(), name='post-saved'),
    path('hid/', HidePostListView.as_view(), name='post-hid'),

    # post viewing and operations
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),  # pk primary key, int integer
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # saving and hiding posts
    path('posts/opt/<int:pk>/<str:option>/', PostOptionView.as_view(), name='post-option-detail'),
    path('posts/optdel/<int:pk>/<str:option>/', PostOptionEdit, name='post-option-edit'),
    path('posts/<int:pk>/<str:user>/save/', UserPostSave, name='post-save'),
    path('posts/<int:pk>/<str:user>/hide/', UserPostHide, name='post-hide'),

    # registration
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),

    # search posts
    path('search', views.search, name='search'),

    # reset db
    path('reset', views.reset)
]

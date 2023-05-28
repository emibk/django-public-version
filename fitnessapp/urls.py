"""fitnessapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from workouts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.workout_list, name="workouts"),
    path('workouts/<int:workout_id>/', views.workout_details, name='workout_details'),
    path('workouts/<int:workout_day_id>/<int:workout_id>/', views.workout_exercises, name='workout_exercises'),
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.sign_up, name='register'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('profile/edit/<str:username>/', views.change_profile, name='change_profile'),
    path('profile/<str:username>/posts/', views.user_posts, name='user_posts'),
    path('profile/<str:username>/reaction_post/<int:post_id>/', views.reaction_post, name='reaction_post'),
    path('profile/<str:username>/posts/new_post/', views.create_post, name='create_post'),
    path('profile/<str:username>/posts/following_posts/', views.followings_posts, name='followings_posts'),
    path('profile/posts/<int:post_id>/<str:username>/<str:view>/new_comment/', views.create_comment, name='create_comment'),
    path('search/', views.following_search, name='following-search'),
    path('profile/<str:username>/followers-unfollowers/', views.my_follows, name='my-follows'),
    path('profile/<str:username>/follow/', views.follow_view, name='follow'),
    path('profile/<str:username>/unfollow/', views.unfollow_view, name='unfollow'),
    path('profile/search-follow', views.following_search, name='following_search'),
    path('add_progress/<int:workout_day_id>//<int:workout_id>/', views.add_progress, name='add_progress'),
    path('profile/<str:username>/progress/', views.progress_list, name='progress_list'),
    path('progress/?filter=date_desc', views.progress_list, name='progress_list'),
    path('payment/', views.payment_view, name='payment'),
    path('payment_successful/', views.payment_successful_view, name='payment_sucessful'),
    path('contact/', views.contact_form, name='contact'),
]

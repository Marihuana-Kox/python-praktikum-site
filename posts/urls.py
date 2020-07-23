from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_posts/", views.all_posts, name="posts"),
    path("group/<str:slug>/", views.group_posts, name="group"),
    path("new/", views.new_post, name="new_post"),
    # Профайл пользователя
    path("follow/", views.follow_index, name="follow_index"),
    path("<str:username>/", views.profile, name="profile"),
    path("<str:username>/<int:post_id>/delete/",
         views.delete_post, name="delete_post"),
    # Просмотр записи
    path("<str:username>/<int:post_id>/", views.post_view, name="post_detail"),
    path("<str:username>/<int:post_id>/edit/",
         views.post_edit, name="post_edit"),
    path("<str:username>/<int:post_id>/comment",
         views.add_comment, name="add_comment"),
    # Фоловер
    path("<str:username>/follow", views.profile_follow, name="profile_follow"),
    path("<str:username>/unfollow", views.profile_unfollow, name="profile_unfollow"),

]

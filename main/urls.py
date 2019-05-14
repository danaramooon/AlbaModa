from django.urls import path
from .views import views,authenticate
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns=[
    path('post/',views.post_list),
    path('post_create/',views.post_create),
    path('post_detail/<int:pk>/',views.post_detail),
    path('post_update/<int:pk>/',views.post_update),
    path('login/',authenticate.login),
    path('jwt_login/',obtain_jwt_token),
    path('register/',authenticate.register),
    path('logout/',authenticate.logout),
    path('post/<int:pk>/comments/',views.CommentListView.as_view()),
    path('post/<int:pk>/comment_create/',views.CommentCreateView.as_view()),
    path('comment_detail/<int:pk>/',views.CommentDetailView.as_view()),
    path('comment_update/<int:pk>/',views.CommentUpdateView.as_view()),
    path('comment_delete/<int:pk>/',views.CommentDeleteView.as_view()),
]

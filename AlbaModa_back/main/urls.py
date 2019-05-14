from django.urls import path
from .views import views,authenticate
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns=[
    path('post/',views.PostList.as_view()),
    path('post_create/',views.post_create),
    path('post_detail/<int:pk>/',views.PostDetail.as_view()),
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

    path('products/',views.ProductListView.as_view()),
    path('products/create/',views.ProductCreateView.as_view()),
    path('products/<int:pk>/',views.ProductDetailView.as_view()),
    path('products/<int:pk>/update/',views.ProductUpdateView.as_view()),
    path('products/<int:pk>/delete/',views.ProductDeleteView.as_view()),
]

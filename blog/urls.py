from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.PostListView.as_view(),name = "home"),
    path('categories/<int:pk>/',views.PostByCategoryView.as_view(),name="post"),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name="detail"),
    path('post/create/',views.PostCreateView.as_view(),name = "create_post"),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(),name = "update"),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name = "delete"),
    path('post/comments/',views.CommentListView.as_view(),name="comment"),
    path('post/<int:pk>/comments/',views.CommentCreateView.as_view(),name="comment_new"),
    path('post/<int:post_pk>/comment/<int:pk>/delete/',views.CommentDeleteView.as_view(),name = "delete_com"),
    path('post/<int:post_pk>/comment/<int:pk>/update/',views.CommentUpdateView.as_view(),name = "update_com"),
    path('search/',views.search,name = "search"),
    path('post/<int:pk>/',views.Like.as_view(),name = "like"),
    path('about/',views.AboutView.as_view(),name="about"),
    path('store/',views.StoreView.as_view(),name="store"),

    path('products/',views.ProductListView.as_view(),name="pro"),
]
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from main.serializers import PostModelSerializer,CommentModelSerializer
from main.models import Post,Comment,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostModelSerializer(posts,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def post_create(request):
    serializer = PostModelSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(owner = request.user,category = Category.objects.get(name = request.data["name"]))
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_detail(request,pk):
    try:
        task=Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    serializer = PostModelSerializer(task)
    return Response(serializer.data)

@api_view(['PUT','DELETE'])
def post_update(request,pk):
    try:
        task=Post.my_post.for_user(owner=request.user).get(pk=pk)
    except Post.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = PostModelSerializer(instance = task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentModelSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Comment.post_comment.for_post(
            post=Post.objects.get(id=self.kwargs["pk"])
        )

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,JSONWebTokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user,post = Post.objects.get(id = self.kwargs["pk"]))

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

class CommentUpdateView(generics.UpdateAPIView,LoginRequiredMixin):
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Comment.post_comment.for_user(
            self.request.user,
            comment=Comment.objects.get(id=self.kwargs["pk"])
        )

class CommentDeleteView(generics.DestroyAPIView,LoginRequiredMixin):
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Comment.post_comment.for_user(
            self.request.user,
            comment = Comment.objects.get(id = self.kwargs["pk"])
        )





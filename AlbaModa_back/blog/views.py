from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Post,Comment,Category,Product
from .forms import SearchForm
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

class PostByCategoryView(ListView):
    #template_name = 'main/categories.html'
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return Post.my_post.category(category = Category.objects.get(id = self.kwargs["pk"]))

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=('title','text','category','img_src')
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ('title','text')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})

    def get_queryset(self):
        return Post.my_post.for_user(owner = self.request.user)

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})

    def get_queryset(self):
        return Post.my_post.for_user(owner = self.request.user)

class CommentListView(ListView):
    model = Comment
    context_object_name = "comments"
    template_name = "main/post_detail.html"

class CommentDetailView(DetailView):
    model = Comment
    context_object_name = "comment"

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('comment', )

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.post = post
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    lookup_field = 'post_pk'

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs[self.lookup_field]})


class CommentUpdateView(LoginRequiredMixin,UpdateView):
    model = Comment
    fields = ('comment',)
    lookup_field = 'post_pk'

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs[self.lookup_field]})

class Like(TemplateView):
    def get_object(self):
        queryset = Post.objects.get(id=self.kwargs["pk"])
        queryset.like +=1
        queryset.save()
        return queryset.like
    template_name = "main/detail.html"

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['title']
            post = Post.objects.all()
            context = {
                'posts': post.filter(title__contains = search),
                'form': form
            }
            return render(request, 'main/post_list.html', context)

class AboutView(TemplateView):
    template_name = "main/about.html"

class StoreView(TemplateView):
    template_name = "main/store.html"

class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "main/store.html"
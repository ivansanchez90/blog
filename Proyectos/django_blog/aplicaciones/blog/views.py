from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Like, Comment
from django.contrib import messages
from .forms import PostForm, UserRegisterForm
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'create'
        })
        return context


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'update'
        })
        return context
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'usuarios/register.html',context)
from site import check_enableusersite
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Cheatsheet, Review, Favorite
from .forms import ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('menu')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/sign_up.html', context)


def menu(request):
    return render(request, 'menu.html')


def cheatsheets_index(request):
    cheatsheets = Cheatsheet.objects.all()
    return render(request, 'cheatsheets/index.html', {'cheatsheets': cheatsheets})


class CheatsheetCreate(LoginRequiredMixin, CreateView):
    model = Cheatsheet
    fields = ['title', 'topic']
    success_url = '/cheatsheets/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def cheatsheets_detail(request, cheatsheet_id):
    cheatsheet = Cheatsheet.objects.get(id=cheatsheet_id)
    review_form = ReviewForm()
    return render(request, 'cheatsheets/detail.html', {
        'cheatsheet': cheatsheet,
        'review_form': review_form,
    })


class CheatsheetUpdate(LoginRequiredMixin, UpdateView):
    model = Cheatsheet
    fields = ['topic']

    def get(self, request, pk):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().get(self, request, pk)
        else:
            return redirect('/cheatsheets/')

    def post(self, request, pk):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().post(self, request, pk)
        else:
            return redirect('/cheatsheets/')


class CheatsheetDelete(LoginRequiredMixin, DeleteView):
    model = Cheatsheet
    success_url = '/cheatsheets/'

    def get(self, request, pk):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().get(self, request, pk)
        else:
            return redirect('/cheatsheets/')

    def post(self, request, pk):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            return super().post(self, request, pk)
        else:
            return redirect('/cheatsheets/')


@login_required
def add_review(request, cheatsheet_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.cheatsheet_id = cheatsheet_id
        new_review.user_id = request.user.id
        new_review.save()
    return redirect('cheatsheets_detail', cheatsheet_id=cheatsheet_id)


class ReviewUpdate(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating', 'comment']


class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = '/cheatsheets/'


@login_required
def add_favorite(request, cheatsheet_id):
    f = Favorite()
    f.cheatsheet_id = cheatsheet_id
    f.user_id = request.user.id
    f.save()
    cheatsheet = Cheatsheet.objects.get(id=cheatsheet_id)
    review_form = ReviewForm()
    return render(request, 'cheatsheets/detail.html', {
        'cheatsheet': cheatsheet,
        'review_form': review_form,
    })


class FavoriteDelete(LoginRequiredMixin, DeleteView):
    model = Favorite
    success_url = '/favorites/'


@login_required
def favorites_index(request):
    favorites = Favorite.objects.all()
    cheatsheets = Cheatsheet.objects.all()
    return render(request, 'main_app/favorite_list.html', {'favorites': favorites, 'cheatsheets': cheatsheets})

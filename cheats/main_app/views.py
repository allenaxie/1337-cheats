from site import check_enableusersite
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Cheatsheet, Review
from .forms import ReviewForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
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


class CheatsheetCreate(CreateView):
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


class CheatsheetUpdate(UpdateView):
    model = Cheatsheet
    fields = ['topic']


class CheatsheetDelete(DeleteView):
    model = Cheatsheet
    success_url = '/cheatsheets/'

def add_review(request, cheatsheet_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.cheatsheet_id = cheatsheet_id
        new_review.user_id = request.user.id
        new_review.save()
    return redirect('cheatsheets_detail', cheatsheet_id = cheatsheet_id)

class ReviewUpdate(UpdateView):
    model = Review
    fields = ['rating', 'comment']
    
class ReviewDelete(DeleteView):
      model = Review
      success_url = '/cheatsheets/'
      
    #   def get_success_url(self):
    #     print('selfffff', self.object)
    #     cheatsheet = self.object.cheatsheet
    #     return reverse('cheatsheets_detail', kwargs={'cheatsheet_id': self.cheatsheet.id})
    

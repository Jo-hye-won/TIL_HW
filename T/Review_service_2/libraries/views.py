from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    books = Book.objects.all()
    context ={
        'books': books
    }
    return render(request, 'libraries/index.html', context)


def detail(reqest, book_pk):
    book = Book.objects.get(pk=book_pk)
    review_form = ReviewForm()
    context = {
        'book': book,
        'review_form': review_form 
    }
    return render(reqest, 'libraries/detail.html', context)


@ login_required
def review_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('libraries:detail', book_pk)
    
    context = {
        'review_form': form
    }
    return render(request,'libraries/detail.html',context)


@ login_required
def review_delete(request, book_pk, review_pk):
    if request.method == 'POST':
        review = Review.objects.get(pk=review_pk)
        if request.user == review.user:
            review.delete()
    return redirect('libraries:detail', book_pk)
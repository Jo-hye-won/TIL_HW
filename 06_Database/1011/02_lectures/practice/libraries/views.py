from django.shortcuts import render, redirect
from .models import Author, Book    
from .forms import BookForm


# Create your views here.
# View 함수가 할 일
def authors(request):
    authors = Author.objects.all()
    # 전체 저자 목록을 보여주기
    # 전체 저자 목록 -> Model
    # model에서 받아와서 사용자한테 어떻게 보여 줄건데?
    # Template
    context = {
        'authors': authors
    }
    return render(request, 'libraries/authors.html', context)


def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    # 나를 참조하고 있는 객체들만 다뤄주는 매니저
    # 역참조 매니저
    # 나를 참조 하고 있는 class명_set 이라는 이름으로 매니저명이 만들어짐
    # 1에 대해서 N개의 책들
    books = author.book_set.all()
    book_count = author.book_set.count()

    book_form = BookForm()
    # Book.objects.filter(author_id=author_pk) # 이렇게 하면 모든 테이블에 있는 정보 다 찾아서 뽑아오는거라서 복잡해짐
    
    context = {
        'author': author,
        'book_form': book_form,
        'books': books,
        'book_count':book_count
    }
    return render(request, 'libraries/detail.html', context)

def book_create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    form = BookForm(request.POST)
    if form.is_valid():
        # book객체에 추가해야할 데이터가 있으니, 
        # 잠시 db에 직접 commit 남기지는 말고 instance만 생성해봐
        book = form.save(commit=False)
        book.author = author
        book.save()
        # detail페이지는 author_pk를 필요로 한다.
    return redirect('libraries:detail', author_pk)
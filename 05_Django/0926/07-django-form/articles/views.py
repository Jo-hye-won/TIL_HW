from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    # if 요청의 메서드가 POST라면: ~ / else: / new로직
    if request.method == 'POST':
        #     create 로직
        form = ArticleForm(request.POST)
        # 유효성 검사
        # 유효성 검사가 통과된 경우 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        
    # 요청의 메서드가 POST가 아니라면(new)
    else:
        form = ArticleForm()    
        # 유효성 검사가 통과되지 않은 경우
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
    
    
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')
   


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 요청의 메서드가 POST라면(update)
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    context = {
        'form' : form,
    }
    
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    return redirect('articles:detail', )

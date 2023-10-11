from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm, Comment


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 특정 게시글의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    # comments = Comment.objects.all()은 게시글에 상관 없이 모든 댓글을 불러옴
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# POST 요청 GET 요청 나눌필요 없음
def comments_create(request, pk):
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    # CommentForm으로 사용자로부터 데이터를 입력 받음
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 사용자가 입력한 값 유효성 검증 끝내고 저장이 되기 전에 article객체 넣고 저장해야함
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)

def comments_delete(request, article_pk, comment_pk):
    # 댓글 조회
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk
    comment.delete()
    return redirect('articles:detail', article_pk )
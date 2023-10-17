from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def main(request):
    # 게시글 전체 정보를 조회
    # Model.manager.querySetAPI

    # SELECT * FROM articles_article ORDER BY pk DESC:
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles':articles
    }
    # BASE_DIR/articles/templates/articles/main.html
    return render(request, 'articles/main.html', context)



def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 물론 생성이 되지는 않는다. 
            # form.save()메서드는 생성된 데이터 인스턴스
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('main')
    else:
        # 게시글 생성을 위한 form이 필요하네...?
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    if request.method == "POST":    
        article = Article.objects.get(pk=article_pk)
        # DELETE FROM articles_article WHERE pk = article_pk;
        article.delete()
    return redirect('main')


def likes(request, article_pk):
    article = Article.objects.get
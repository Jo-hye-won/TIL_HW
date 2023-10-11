# views.py
def detail(request, __(a)__):
    article = get_object_or_404(Article, pk=article_pk)

    comment_form = CommentForm()
    context_data = {
        'article': article,
        __(b)__,
    }
    return render(request, 'eithers/detail.html', __(c)__)

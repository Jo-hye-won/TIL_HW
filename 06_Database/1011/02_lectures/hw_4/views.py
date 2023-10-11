def detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    comment_form = CommentForm()

    count_a = question.comment_set.filter(pick=False).__(a)__
    count_b = question.comment_set.filter(pick=True).__(a)__
    total_count = __(b)__

    per_a = 0
    per_b = 0
    if __(c)__:
        per_a = round(count_a / total_count * 100, __(d)__)
        per_b = round(count_b / total_count * 100, __(d)__)

    comments = question.comment_set.__(e)__
    context = {
        'question': question,
        'comment_form': comment_form,
        'count_a': count_a,
        'count_b': count_b,
        'per_a': per_a,
        'per_b': per_b,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

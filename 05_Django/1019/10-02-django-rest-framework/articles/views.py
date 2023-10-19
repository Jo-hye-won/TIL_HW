from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404 # 참고 
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article) # 참고
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)  # 참고
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        #  partial=True => 데이터 일부분만 수정 가능
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # 예외가 발생했을 때의 옵션 리턴할수 있도록 raise_exception=True 하는 것 가능
        # HTTP 상 당연히 해줘야 할 것들에 대한 추가 옵션
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment) # 참고
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


# articles/views.py
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)  # 참고
    if request.method == 'GET':        
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save() # comment 인스턴스에 article 있기 때문에 넘겨주지 않아도 된다 
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Comment, pk=article_pk)  # 참고
    serializer = CommentSerializer(data=request.data)
    # DRF가 아닌 일반 django에서 1:N 관계의 데이터 생성시와
    # 로직이 변경되었다. 
    if serializer.is_valid(raise_exception=True):
        # commit=False 라는 작업이 필요했다. -> save()의 역할이
        # DB에 사용자가 작성한 데이터를 통해 생성, 수정하는 역할이었기 때문에
            # 사용자가 필드에 작성하지 않은 참조 대상의 PK값을 저장할 수 없?????
            # 무결성 에러가 발생했었따. 
        # DRF 작업자가 생각해보니 어차피 serializer에 이미
        # Model에 대한 정보가 다 포함되어 있는데 field와 적절한 데이터를
        # 넘겨주면서 save()하면 편하지 않을까?
        serializer.save(article=article) 
        # article이라는 변수에 article 인스턴스 값 넣어줌
         # article = 키워드 인자
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 조회는 가능하면서 유효성 검사에서는 빠져야 하는 친구들 => 읽기 전용 필드

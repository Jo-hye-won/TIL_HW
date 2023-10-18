from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticlesListSerializer, ArticlesSerializer

# @api_view(['GET'])
# def article_list(request):
#     articles = Article.objects.all()
#     serializer = ArticlesListSerializer(articles, many=True)
#     return Response(serializer.data)

# api_view 데코레이터에 넘겨준 값 이외의 method로 요청이 들어오면
# 405 method not allowed status code 를 반환함

# drfview함수에서는 @api_view(['GET']) 가 있어야 한다. (약속임)
# GET에 대한 요청만 통과할 수 있다. GET이 기본값이라서 안넣어도 되지만 넣자 
@api_view(['GET', 'POST'])
def article_list(request):
    # request.method == 'POST'를 조건으로 잡고 나머지 else처리였는데
        # POST 이외 요청에 대해서는 DB에 영향을 미치지 않는 HTML반환처리
    # 얘는 왜 GET 이랑 POST를 if elif로 처리하나요?
        # GET일 때, POST일 때 정해진 상황에 대해 정해진 처리만 하면 그만.
    if request.method == 'GET':
        # [<Article Object (1)>, <Article Object(2)>, ...]
        articles = Article.objects.all()
        # articles에 들어있는 데이터들을 HTML에 그려서 반환
        # articles에 들어있는 데이터들을 JSON으로 변환해서 반환
        # 다중 데이터 =>  many=True
        # serializer 이거 자체는 객체다. 
        serializer = ArticlesListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # ModelForm에다가 request.POST를 넣을떄는 첫번째 인자로 넣으면 됐는디...
        # 야는 왜,,, 키워드 인자로 넣어야하나....
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def article_datail(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     serializer = ArticlesSerializer(article)
#     return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':    
        serializer = ArticlesSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # form = ArticleFrom(request.POST, instance=article)
        serializer = ArticlesSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
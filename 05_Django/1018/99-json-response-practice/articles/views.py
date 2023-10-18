from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):
    #쿼리셋 
    articles = Article.objects.all()
    # 쿼리셋 결과를 받아서 모델폼을 거쳐서받은결과물을
    serializer = ArticleSerializer(articles, many=True)
    # context에 담는게 아니라 변환을 하고 있음 
    # 그 변환한 값을 응답받고 있음
    # 응답을 하겠다는 목적은 같은데 방법이 달라짐
    return Response(serializer.data)

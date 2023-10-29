from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 댓글 만들거나 상세내용 확인하거나 할때 필요한 정보 만들어주는 애
    # 댓글 만들때, Article에 대한 정보도 필요함
     # 근데 사용자가 입력하지는 않음

    # 댓글 조회시, Article에 대한 정보 필요함
class CommentSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('id','title',)

    # override
    # article이라는 변수는?
        # class Comment에 작성했던 article 변수에 해당하는 내용
        # fields 에 작성될 article의 역할을 바꿔줌
    
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('article', 'content', 'created_at', 'updated_at')
        # fields = '__all__'
        # read_only_fields = ('article',)

# articles/serializers.py
class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializerForArticle(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('content',)
    # 나를 참조하고 있는 모든 댓글 정보 다 가져 오겠다.
    # serializer의 목적 : 가지고 온 데이터를 사용자에게
                        # 어떻게 보여줄 것인지 정의
    comment_set = CommentSerializerForArticle(many=True, read_only=True)
    # 내가 마음대로 정의한 변수 명. 다른 이름으로 해도 상관없음
    # comment_set와 같이 역참조 매니저명은 django가 기존에 정의해놓은 것

    # 'comment_count' 해당 변수는 내가 새롭게 정의한 것
    # comment_count 변수에 할당되어야 할 값도 내가 정의 해줘야 함.
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

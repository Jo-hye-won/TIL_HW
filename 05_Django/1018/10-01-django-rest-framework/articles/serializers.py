from rest_framework import serializers
from .models import Article

# ModelForm이 하는 일 : Model 정보를 토대로, 사용자에게 Model과 관련된 어떠한 정보를 보여줌
            # 혹은 해당 Model의 인스턴스 정보를 생성, 수정할 수 있게 해줌

# ModelSerializer가 하는 일 : Model 정보를 토대로, 사용자에게 Model과 관련된 어떠한 정보를 보여줌
            # 혹은 해당 Model의 인스턴스 정보를 생성, 수정할 수 있게 해줌


class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
        # exclude = ('created_at', ')



class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
'''
사용자가 실제 웹 페이지 내에서 파일을 조회 할 수 있도록 하기 위해선 
업로드 된 Media 파일에 대한 URL 을 생성 해주는 설정이 필요하다. 
'''
# 다음 urls.py에 설정값을 작성하시오.
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, documet_root = settings.MEDIA_ROOT)

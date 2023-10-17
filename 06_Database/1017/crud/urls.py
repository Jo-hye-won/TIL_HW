"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from articles import views as articles_views
# from articles import views as acocunts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 앱마다 분리해서 관리
    # url로 요청이 들어왔을 때, 실행할 view 함수가 정의된 위치
    # 모든 app이 views로 통일되어있기 때문에...
    path('accounts/', include('accounts.urls'))
]

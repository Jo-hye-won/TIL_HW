#1.  static 파일 기본 설정
# 추가 파일 경로 지정해주기 위해서는
STATICFILES_DIRS = [
    BAE_DIR / 'assets'   
]

#2.  media 파일 기본 설정
MEDIA_ROOT = BAE_DIR / 'uploaded_files'

MEDIA_RUL = 'media // '
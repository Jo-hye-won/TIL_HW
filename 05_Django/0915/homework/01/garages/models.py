from django.db import models

# Create your models here.
# 파이썬 클래스 정의 => 아이디어 스케치
class Garage(models.Model):
    # id  컬럼은 직접 정의안해도 알아서 해줄거임
    # 장소(주소)
    location = models.CharField(max_length=200)
    # 용량(주차 가능 수량)
    capacity = models.IntegerField()
    # 주차 가능 여부
    is_parking_avaliable = models.BooleanField()
    # 여는시간 / 닫는시간
    opening_time = models.TimeField()
    # Field들 뒤에 호출 () 생략하는 경우 있는데...
        #  vairable = class 할당이 된다()
    # class_variable = models.class() 인스턴스 할당해야함!!
    closing_time = models.TimeField()


# makemigrations -> 설계도 작성해야 함
# migrate -> 집(table) 만들기 

# 조회
# ORM -> python objet 다루는 법
# myModel ClassName.manager.QuerySet API
garages = Garage.objects.all()
print(garages)

# 생성
# python Object
# 객체 하나 생성(인스턴스 생성)
garage = Garage()

garage.location = '부산시 강서구'    # 200글자 제한 string
garage.capacity = 10                # integer
garage.is_parking_avaliable = True  # Boolean
garage.opening_time = '07:00'
garage.closing_time = '23:00'
print(garage.location)

# save 메서드 호출
garage.save()

# QuerySet API
# 생성 완료된 경우, 완료된 객체 반환
garage_2 = Garage.objects.create(
    location ='경상남도 창원시',
    capacity=20,
    is_parking_avaliable=False,
    opening_time='07:00',
    closing_time='23:00'
)

# 삭제
# 삭제 완료된 경우, 완료된 객체 반환
garage_2.delete()


# garages = <querySet []>
# 파이썬 리스트랑 똑가티 쓸 수 있다.



name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in range(5):  # 이 for문은 필요가 없는 것 같다
            # map이 알아서 리스트의 모든 요소에 적용을 하니까?
    def create_user(name, age, address):
            user_info={
                'name' : name,
                'age' : age,
                'address' : address
            }
            print(f'{name}님 환영합니다!')
            return user_info


print(list(map(create_user,name, age, address)))
 # iterable한 요소중의 하나인 list 형식의 
 # name,age,address의 모든 요소에 
 # create_user 함수를 적용해서
 # 그 결과를 map object로 반환하고 
 # 그걸 리스트로 만들어서 출력함

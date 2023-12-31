
#### 배낭 짐싸기(Knapsack) 문제 유형
1. 0-1 Knapsack
: 배낭에 물건을 통째로 담아야 하는 문제
   물건을 쪼갤 수 없는 경우
   
< 완전 검색 방법>
- 완전 검색으로 물건들의 집합 S에 대한 모든 부분집합을 구함
- 부분집합의 총무게가 W를 초과하는 집합들은 버리고, 나머지 집합에서 총 값이 가장 큰 집합 선택
- 물건의 개수가 증가하면 시간 복잡도가 지수적으로 증가
 
< 탐욕적 방법>
- 값이 비싼 물건부터 채운다 -> 최적이 아니다 
- 무게가 가벼운 물건부터 채운다 -> 최적해를 구할 수 없다. 
- 무게 당 값이 높은 순서로 물건을 채운다 -> 역시 탐욕적 방법으로 최적해를 구하기 어렵다.


2. Fractional Knapsack
: 물건을 부분적으로 담는 것이 허용되는 문제
   물건을 쪼갤 수 있는 경우 


#### 회의실 배정하기 
- 김대리는 소프트웨어 개발팀들의 회의실 사용신청을 처리하는 업무를한다. 
  이번 주 금요일에 사용 가능한 회의실은 하나만 존재하고 다수의 회의가 신청된 상태이다
  회의는 시작 시간과 종료 시간이 있으며, 회의 시간이 겹치는 회의들은 동시에 열릴 수 없다.
  가능한 많은 회의가 열리기 위해서는 회의들을 어떻게 배정해야 할까?
  
- 시작시간고 종료시간이 있는  n개의 활동들의 집합에서 서로 겹치지 않는 최대개수의 활동들의 집합 S를 구하는 문제
- 양립 가능한 활동들의 크기가 최대가 되는 S0,n+1의 부분집합을 선택하는 문제
- 종료 시간 순으로 활동들을 정렬한다.



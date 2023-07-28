# 02_pjt

## A. 데이터 전처리 _ 데이터 읽어오기
### Numpy 활용해서 csv file 불러오기
```bash
# # Numpy 활용해서 csv file 불러오기
# def file_open_by_numpy():
#     np_arr = np.loadtxt('Data/NFLX.csv', delimiter=",", encoding='cp949', dtype=str)
#     return np_arr


# arr = file_open_by_numpy()
# print(arr)

# # 데이터 프레임 생성하기
# df = pd.DataFrame(arr)
# df


# 그런데 [‘Date’, ‘Open’, ‘High’, ‘Low’, ‘Close’ ] 필드만 읽어오도록 구성해야 하니까
# 특정 범위의 열만 가져오기(True/False 배열을 이용해서 True인 행만 가져오기)
# df.loc[:,[True,True,True,True,True,False,False]]


# 날짜 데이터를 필터링이 가능하게 하기 위해서 
# # 데이터 타입을 변경하기(to_datetime() 활용해서 하기!)
# df["Date"] = pd.to_datetime(df["Date"])

# # 2021-01-01 이후의 데이터만 선택해서 df_2021 만들기
# df_2021 = df[df["Date"] >= "2021-01-01"]

# df_2021

```
np_arr = np.loadtxt('Data/NFLX.csv', delimiter=",", encoding='cp949', dtype=str)
> 를 작성할 때 유의할 점이 'Data/NFLX.csv'를 현재 내 파일의 위치에서 찾고 있어서 내가 작성하고 있는 파일이 파일을 찾을 Data 파일과 같은 위치에 있어야 한다. 

- 특정 범위의 열만 가져오기(True/False 배열을 이용해서 True인 행만 가져오기) 방법을 사용해서는 결과가 잘 나왔는데 

> df.loc[:, '나이':'직업'] 특정 범위의 열 가져오기로는 결과가 안나옴
다 하고 다시 시도해보자!

## 종가데이터 처리 안되서 데이터 불러오는거 다른걸로 해서 다시 해보자!
```bash
# CSV 파일 경로
csv_path = "Data/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(0,5))

# DataFrame 출력
df
```

> 이걸로 하니깐 오류 없이 추출됨 ... 왜지?

### 데이터 분석
dt.to_period 랑 groupby 사용해서 월별로 묶어야 함
dt.to_period = 달을 알아서 구분해줌



# ★★★ 저장을 잘하자 ★★★ 날려서 다시했다 ★★★




> 오...이런방법이..

```python
# 2021년 데이터만 추출하기
df_2021 = df_after_2021[(df_after_2021["Date"] >= "2021-01-01") & (df_after_2021["Date"] < "2022-01-01")]

# 월 컬럼을 만들어 주기
df_2021['month'] = df_2021['Date'].dt.month

# 월별 평균 값 구하기
df_mean = df_2021.groupby(by='month').mean()
df_mean

# 2022년 데이터만 추출
df_2022 = df_after_2021[df_after_2021["Date"] >= "2022-01-01"]
df_2022

# 2022년 월 데이터 추출
df_2022['month'] = df_2022['Date'].dt.month

# 2022년 월별 데이터 평균 구하기
df2_mean = df_2022.groupby(by='month').mean()
df2_mean

# 2021년 데이터와 2022년 데이터 합치기
df_total = pd.concat([df_mean, df2_mean])
df_total

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(df_total['Date'], df_total['Close'])

# 그래프 제목 설정
plt.title('Monthly Average Close Price')

# x축 레이블 설정
plt.xlabel('Date')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# y축 레이블 설정
plt.ylabel('Average Close price')

# 그래프 표시
plt.show()
```
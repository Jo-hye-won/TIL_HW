import math

start = [127, 63.5]
end = [254, 127]
a = abs(end[0]-start[0])
b = abs(end[1]-start[1])

r = math.sqrt(a**2 + b**2)
# print(r)

# 아크 코사인 써서 구하는 방법
# x = ((b**2 + r**2) - a**2) /(2*b*r)
# print(x)
# seta = math.acos(x)
# print(math.degrees(seta))

# 아크탄젠트 써서 구하는 방법
seta = math.atan(b/a)
print(seta,'seta')
print(90-math.degrees(seta))
seta2 = math.tan(b/a)
print(seta2,'s')
# # 아크사인 써서 구하는 방법
# seta = math.a(b/r)
# # print(seta))
# print(90-math.degrees(seta))
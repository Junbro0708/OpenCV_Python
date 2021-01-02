# 파이썬 기초

a = 5

if a == 3:
    print("준형 바보")
elif a == 4:
    print("준형 최고")
else:
    print("준형 멋쟁이")

print(type(a))

a = float()

print(type(a))

# 리스트 (배열)

a = 3
arr = [1, 2, 3, 4, 5]  # 리스트 -> 변경이 가능한 배열
arr[2] = 100
print(arr[2])  # 인덱스

# 튜플 -> 변경이 불가능한 배열 / 서버에서 데이터를 전송할 때의 데이터들은 모두 튜플로 전달됨. 손상방지 차원

tuple_t = (1, 2, 3, 4, 5)
print(tuple_t[1])

# 세트 -> 순서가 없음 / 같은 숫자가 여러개여도 하나로 인정

set_s = {1, 2, 3, 4, 5, 5, 3, 4}
print(set_s)

# 딕셔너리 -> 키와 밸류의 쌍으로 이루어짐 Key-Value

dict_d = {'key': 'value',
          '강아지': '멍멍',
          '고양이': '야옹'}

print(dict_d)
print(dict_d['강아지'])

# ----------------------------------------------
# 반복문 while

b = 0

while b < 10:
    print(b)
    b += 1

# 반복문 for

for i in range(0, 3, 1):  # 0부터 3까지 1씩 증가
    # in은 반복 가능한 객체를 i에 넣어준다는 것
    # 반복 가능한 객체 : iterable 객체
    # 반복 가능한 객체는 나열 되어있는 자료 객체 => 리스트, 튜플, 세트, 딕셔너리
    print(i)

list_l = [60, 20, 90]
sum_s = 0

for i in list_l:
    sum += i
print(sum)
print(len(list_l))

# 반복문을 사용한 구구단 출력
c = 3

for i in range(1, 10, 1):
    print("{} x {} = {}".format(c, i, c * i))  # 문자열 내장함수 (포맷팅)

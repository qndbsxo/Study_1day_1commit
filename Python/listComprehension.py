# 복잡한 리스트 컴프리헨션 생성금지

# badExample
# 다음과 같이 여러 개의 if 조건이 이 있다면 리스트 컴프리헨션 대신 루프를 사용하는 것을 고려할 수 있다.
ages = [1, 34, 5, 7, 3, 57, 356]
old = [age for age in ages if age > 10 and age < 100 and age is not None]\

# goodExample
# 한 라인에 많은 일이 일어나면 읽기 어렵고 오류가 발생하기 쉽다.
ages = [1, 34, 5, 7, 3, 37, 356]
old = []
for age in ages:
    if age > 10 and age < 100:
        old.append(age)
print(old)


# REFERENCE
# 클린 파이썬: 수닐카필

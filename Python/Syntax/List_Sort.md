# 15.List(리스트) - 리스트 정렬

## 1. list 본체 정렬

- reverse: 리스트를 거꾸로 뒤집는다(desc 정렬이 아님)

``` python
>>> a = [1, 10, 5, 7, 6]
>>> a.reverse()
>>> a
[6, 7, 5, 10, 1]
```

- sort: 정렬, 기본값은 오름차순 정렬, reverse옵션 True는 내림차순 정렬

``` python
>>> a = [1, 10, 5, 7, 6]
>>> a.sort()
>>> a
[1, 5, 6, 7, 10]
>>> a = [1, 10, 5, 7, 6]
>>> a.sort(reverse=True)
>>> a
[10, 7, 6, 5, 1]
```

- sort의 key 옵션, key 옵션에 지정된 함수의 결과에 따라 정렬, 아래는 원소의 길이

``` python
>>> m = '나는 파이썬을 잘하고 싶다`
>>> m = m.split()
>>> m 
['나는', '파이썬을', '잘하고', '싶다']
>>> m.sort(key=len)
>>> m
['나는', '싶다', '잘하고', '파이썬을']
```

# 2.list 정렬된 겨로가 반환

- 정렬된 결과를 반환하는 함수는 본체는 변형하지 않습니다.
- sorted: 순서대로 정렬, 정렬된 리스트를 반환

``` python
x = [1, 11, 2, 3]
y = sorted(x)
print(x)
>>> [1, 11, 2, 3]
print(y)
>>> [1, 2, 3, 11]
```

- reversed: 거꾸로 뒤집기, iterable한 객체를 반환, 확인을 위해서는 list로 한번 더 변형 필요

``` python
x = [1, 11, 2, 3]
y = reversed(x)
print(x)
>>> [1, 11, 2, 3]
print(y)
>>> <list_reverseiterator object at 0x1060c9fd0>
print(list(y))
>>> [3, 2, 11, 1]
```

# REFERENCE
https://wikidocs.net/16041

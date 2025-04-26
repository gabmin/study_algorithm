## 개인적인 기록

### 자료구조의 시간복잡도
- 이진 탐색: O(logN)
- 버블 정렬: O(N^2)
- 선택 정렬: O(N^2)
- 삽입 정렬: O(N^2)
- 병합 정렬: O(NlogN)
- 이진 트리: O(logN)
- 힙: O(logN)

### 문자열 확인 내장 함수
*str.isalpha()*

```python
print("a".isalpha())    # True
print("1".isalpha())    # False

s = "abcdefg"
print(s[0].isalpha())   # True
```

<br/>

### 문자 빈도수 구하기 문제

아스키 코드를 활용하여 아스키 값을 인덱스로 사용하는 방법

```python
# 내장 함수 ord() 이용해서 아스키 값 받기
print(ord('a'))               # 97
print(ord('a') - ord('a'))    # 97-97 -> 0
print(ord('b') - ord('a'))    # 98-97 -> 1

chr(97) == 'a'
chr(0 + ord('a')) == 'a'
chr(0 + 97) == 'a'
chr(1 + 97) == 'b'
```

<br/>

## 교집합 구하기
```python
print(set([1, 3, 5, 7]) & set([3, 7])) # [3, 7]
```

## all 내장 함수
순회한 결과가 모두 참인지 아닌지 판단하는 함수 (자바스크립트의 Some 비슷)

```python
if all(len(set(code) & set(q[i])) == ans[i] for i in range(len(q))):

# for i in range(len(q)) 에서 len(set(code) & set(q[i])) == ans[i] 결과 값이 모두 참인지 판단하는 함수
```

## zip 내장 함수

```python
numbers = [1, 2, 3]
letters = ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

# (1, 'A')
# (2, 'B')
# (3, 'C')
```





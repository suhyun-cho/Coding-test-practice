
## greedy 알고리즘 문제 - 잃어버린 괄호
2020-12-01

#### 문제설명
세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
<br>
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.<br>

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.<br>

* 작은값을 만들기 위해서는 작은수에서 큰수를 빼면됨
* ' - ' 기준으로 괄호를 쳤을 때 최솟값이 됨.
    * split('-') 으로하면 ' - ' 기준으로 문자 나뉨


```python
s=55-(50+40)
s
```




    -35




```python
a=input().split('-')
a
```

    55-50+40-30+20





    ['55', '50+40', '30+20']




```python
a[1].split('+')
```




    ['50', '40']




```python
# 숫자 하나만있을경우
[int(x) for x in a[0].split('+')]
```




    [55]




```python
# 숫자와 '+' 문자 둘다있을경우
[int(x) for x in a[1].split('+')]
```




    [50, 40]




```python
# 합계
sum([int(x) for x in a[1].split('+')])
```




    90




```python
# '-' 를 기준으로 양수만 더한값 리스트
num=[]
for i in range(len(a)):
    num.append(sum([int(x) for x in a[i].split('+')]))
print(num)
```

    [55, 90, 50]



```python
num=[]
for i in range(len(a)):
    num.append(sum([int(x) for x in a[i].split('+')]))

answer=num[0]
for j in range(1,len(num)):  # j=1,2
    answer=answer-num[j]
print(answer)
```

    -85


-------------------------------------------------------
#### 수현's 최종코드
* Point !!
    * '-' 를 기준으로 split() 함수로 식을 분리한다는것이 첫번째 포인트
    * 그다음 '+' 를 기준으로 다시 split() 으로 또 분리해서 덧셈연산을 하는것이 두번째 포인트


```python
a=input().split('-')
num=[]
for i in range(len(a)):
    num.append(sum([int(x) for x in a[i].split('+')]))
    
answer=num[0]
for j in range(1,len(num)):  # j=1,2
    answer=answer-num[j]
print(answer)
```

    55-50+40-30+20
    -85



```python

```

# https://www.acmicpc.net/problem/1668

#탐색문제

# 첫째 줄에 왼쪽에서 봤을 때 보이는 개수, 둘째 줄에 오른쪽에서 봤을 때 보이는 개수를 출력한다.

def ascending(array):
  now = array[0]
  cnt = 1
  for i in range(1,len(array)):
    if array[i] > now:
      now = array[i]
      cnt += 1
  return cnt

n = int(input())
array =  []
for _ in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))


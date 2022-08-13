#https://www.acmicpc.net/problem/1874
#스택문제

#첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

n=int(input())

cnt = 1
stack = []
result = []

for i in range(1,n+1): #데이터 개수만큼 반복
  data = int(input())
  while cnt  <= data:
    stack.append(cnt)
    cnt += 1
    result.append('+')
  if stack[-1] == data: #스택의 최상위 데이터와 data가 같을 때만 출력
    stack.pop()
    result.append('-')
  else: #불가능한 경우
    print('NO')
    exit(0)

print('\n'.join(result))
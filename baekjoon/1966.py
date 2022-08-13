#큐문제
#https://www.acmicpc.net/problem/1966


n=int(input())

for i in range(1,n+1):
  n,m = map(int,input().split())
  #n=4 m=2
  #1132
  a = list(map(int,input().split())) #중요도
  q = [(i, idx) for idx, i in enumerate(a)]
  cnt = 0
  while True:
    if q[0][0] == max(q, key=lambda x: x[0])[0]:
      cnt += 1
      if q[0][1] == m:
        print(cnt)
        break
      else:
        q.pop(0)
    else:
      q.append(q.pop(0))
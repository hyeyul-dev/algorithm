#스택,구현, 그리디 문제

#https://www.acmicpc.net/problem/5397

#강산이가 백스페이스를 입력했다면, '-'가 주어진다. 
#이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 
#화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 
#나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

# -, <
#<<BP<A>>Cd-
n=int(input())

for i in range(n):
  pwd = str(input())
  left_stack = []
  right_stack = []
  for j in pwd:
    if j == '<':
      if left_stack:
        right_stack.append(left_stack.pop())
    elif j == '>':
      if right_stack:
        left_stack.append(right_stack.pop())
    elif j == '-':
      if left_stack:
        left_stack.pop()
    else:
      left_stack.append(j)
  left_stack.extend(reversed(right_stack))
  print(''.join(left_stack))
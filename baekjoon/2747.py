#https://www.acmicpc.net/problem/2747


#피보나치 수열

# 0 1 1 2 3 5 8 13 21 34 55

n = int(input())

def fibonacci(num):
  if num-2 < 0:
    return num
  return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(n))

#-> 이렇게 하면 시간초과가 남. 시간복잡도: O(2^n)



n = int(input())

a,b = 0,1

while n > 0:
  a,b = b, a+b
  n -= 1

print(a)
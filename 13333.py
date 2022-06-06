


n=int(input())
a=sorted(map(int,input().split()))
k=n
while k>0:
    if a[n-k]>=k:   #k번 이상 인용된 논문이 k편 이상이여하므로 뒤에서부터 k번째의 인덱스가 k보다 크면 된다.
        break
    k-=1
print(k)
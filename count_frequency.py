from collections import Counter
arr= list(map(int, input().split()))
arr=sorted(arr)
frq=Counter(arr)
print(dict(frq))
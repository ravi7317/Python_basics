def rotate_arr(arr,k):
    n = len(arr)
    k %= n
    return arr[k:]+arr[:k]
arr=list(map(int, input().split()))
k= int(input())
print(rotate_arr(arr,k))
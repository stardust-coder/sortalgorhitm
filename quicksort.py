import random

def partition(A,p,r):#O(n)時間
    x = A[p]
    i = p-1
    j = r+1
    while True:
        while True:
            j -= 1
            if A[j]<=x:
                break
        while True:
            i += 1
            if A[i]>=x:
                break
        #print(i,j)
        if i < j:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp #A[i]とA[j]を入れ替え
            #print("if文内部 入れ替え後", A)
        else:
            return j

def quicksort(A,p,r):#A:配列,p:先頭, r:末尾
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)
    return A

def randomized_quicksort_a(A,p,r):#A:配列,p:先頭, r:末尾
    random.shuffle(A)
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)
    return A

def randomized_partition(A,p,r):
    i = random.randint(p,r)
    tmp = A[i]
    A[i] = A[p]
    A[p] = tmp #A[i]とA[p]の値を入れ替える
    return partition(A,p,r)

def randomized_quicksort_b(A,p,r):#A:配列,p:先頭, r:末尾
    if p<r:
        q = randomized_partition(A,p,r)
        randomized_quicksort(A,p,q)
        randomized_quicksort(A,q+1,r)
    return A

A = [5,3,2,6,4,1,3,7]#初期配列
n = len(A)
quicksort(A,0,n-1)
randomized_quicksort_a(A,0,n-1)
randomized_quicksort_b(A,0,n-1)#平均O() 最悪O(n^2)

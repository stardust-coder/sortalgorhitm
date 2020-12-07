#選択問題はソートはO(nlogn)だが実はO(n)で解ける！！

def minimum(n,A):
    return min(A)
#ポイント：n-1回の比較は絶対必要であり, 最適

def randomized_select(A,p,r,i):#A[p〜r]の中でi番目に小さい要素を返す
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)#quick sortと一緒！
    k = q-p+1
    if i <= k:
        return randomized_select(A,p,q,i)#左側
    else:
        return randomized_select(A,q+1,r,i-k)#右側
    return
#平均的な計算量は?->平均的にO(n)

#最悪でも線形時間にしたい
def select():
    #O(1):ざっくり５こずつ分割

    #O(n):n/5この各グループをソートしそれぞれの中央値を求める

    #T(n/5):再帰的にn/5この中央値たちの中央値xを求める

    #O(1)元の配列をxによって分割->右側の要素数の下界は3n-60/10こ


    return

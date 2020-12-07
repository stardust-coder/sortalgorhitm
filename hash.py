def hash(k):
    return k%m

#チェイン法（deleteするときはおすすめ）


#オープンアドレス法（メモリが食わないからおすすめ）

#衝突回避のための近似一様ハッシュ関数
def linear_hash(m,k,i):#線形探査
    return (hash(k)+i)%m
    #異なる探査列がm通りしか実現できない・primary clusteringが起きる

def square_hash():#2次関数探査
    c1 = 1
    c2 = 1
    res = (hash(k)+c1*i+c2*i*i)%m
    return
    #linearよりはマシだが、secondary clustering

def double_hash():#ダブルハッシュ
    res = (hash_a(k)+i*hash_b(k))%m
    return res

def hash_search(T,k):
    m = len(T)
    i = 0
    while(T[j]!=None or i!=m):
        j = hash(m,k,i)
        if T[j] == k:
            return j
        i += 1
    return None

#運がめちゃんこ悪いと・・・平均検索時間がΘ(n)
#Universal Hashing:ハッシュ関数をランダムに選ぼう

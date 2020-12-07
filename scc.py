#強連結成分分解
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

V,E = map(int,input().split())#頂点,エッジ数
edge = np.array([input().split() for _ in range(E)], dtype = np.int64).T
print(edge)
tmp = np.ones(E, dtype = np.int64).T#重みは関係ないからとりま全部1
graph = csr_matrix((tmp, (edge[:] -1)), (V, V))
print(graph)

num, components = connected_components(graph, directed=True, connection="strong")#入力は疎行列形式, direction=Trueは有向グラフ
print(num)#出力は成分数, 頂点ごとにどの強連結成分に属するか
print(components)

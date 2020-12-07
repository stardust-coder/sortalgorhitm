#ダイクストラ法
import copy
import numpy as np

def input_graph():
    s, e = map(int,input().split())#s:エッジ数, e:ノード数
    E = []
    G = np.zeros([s+1,s+1],dtype=int)
    Adj = [[] for _ in range(s+1)]
    for _ in range(e):
        start,goal,cost = map(int,input().split())
        E.append([start,goal,cost])
        G[start][goal] = cost
        Adj[start].append(goal)
    return E,G,Adj


def dijkstra(s):#多分O(n^2)
    E,G,Adj = input_graph()
    d = [float("inf") for _ in range(len(G)-1)]
    p = [0 for _ in range(len(G)-1)]#sからiまでの最短路においてiの直前に位置する節点を示すために用いられる
    temp = []
    for item in E:
        temp.append(item[0])
        temp.append(item[1])
    V = list(set(temp))
    Sbar = copy.deepcopy(V)
    S = []
    d[s] = 0
    k=0#反復回数
    while set(S) != set(V):
        k += 1
        print("{}回目".format(k))
        #比較
        minval = min([d[remained_node] for remained_node in Sbar])#ヒープを使うと取り出すのにO(logn)時間
        v = d.index(minval)
        Sbar.remove(v)
        S.append(v)
        #更新
        for node in Adj[v]:
            if d[node] > d[v]+G[v][node]:
                d[node] = d[v]+G[v][node]
                p[node] = v
    saitanrogi = [[p[i],i] for i in range(1,len(p))]#最短路木も出力
    return d,saitanrogi

s = 0
#print(dijkstra(s))

#重みなしの場合（＝重みをすべて１とする）
#ポイント：BFSで行ける！

from collections import deque
def dijkstra_bfs(G,s):#Gは隣接リスト
    d = [float("inf") for _ in range(len(G))]
    pi = [None for _ in range(len(G))]
    color = [0 for _ in range(len(G))]
    d[s] = 0
    color[s] = 1
    Q = deque([])
    Q.append(s)
    k=0
    while Q != deque([]):
        k += 1#反復回数
        print("{}回目".format(k))
        u = Q.popleft()
        for v in G[u]:
            if color[v] == 0:#0が白, 1が灰, 2が黒
                color[v] = 1
                d[v] = d[u] + 1
                pi[v] = u
                Q.append(v)
        color[u] = 2
        #print(d,color,Q,pi)
    return d

G = [[],[],[]]#隣接リスト
print(dijkstra_bfs(G,0))

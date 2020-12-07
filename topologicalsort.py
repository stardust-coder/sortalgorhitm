#トポロジカルソートO(n+m)
#閉路のない有向グラフ(DAG)->絶対始点が先、終点が後となっているソート
#半順序に、矛盾しない全順序の可能性を１つ与えることに相当！
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

label_list = ["undershorts","pants","belt","shirt","tie","jacket","socks","shoes","watch"]
n, m = map(int, input().split())#nは頂点数, mは辺の数
graph = [[] for _ in range(n)]
digraph = nx.DiGraph()#可視化用
digraph.add_nodes_from(label_list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    #graph[b-1].append(a-1)  # 有向グラフなら消す
    digraph.add_edges_from([(label_list[a],label_list[b])])
#print(graph)  # [[2, 3, 5], ..., [1, 3, 4]]

#0が白,1が灰,2が黒
def topological_sort(G):#Gは隣接リストとする
    L = []
    color = []
    for u in range(len(G)):
        color.append(0)
    for u in range(len(G)):
        if color[u] == 0:
            L,color,res = visit(u,G,L,color)
            if res == False:
                break
    return L

def visit(u,G,L,color):
    if color[u] == 1:
        return L,color,False
    elif color[u] == 2:
        return L,color,False
    else:
        color[u] = 1
        for v in G[u]:
            visit(v,G,L,color)
        color[u] = 2
        L.insert(0,u)
        return L, color, True

ans = topological_sort(graph)
print(ans)

ans_label = [label_list[i] for i in ans]
print(ans_label)

pos = {
        n: (np.cos(2*i*np.pi/9), np.sin(2*i*np.pi/9))
        for i, n in enumerate(digraph.nodes)
    }
nx.draw_networkx(digraph,pos,node_color="lightblue",node_size=1000,with_labels=True)
#plt.savefig('digraph_sample.png')
#plt.show()

#結果図示用
ans_digraph = nx.DiGraph()
ans_digraph.add_nodes_from(ans_label)
ans_edge = []
for i in range(len(ans_label)-1):
    ans_edge.append((ans_label[i],ans_label[i+1]))
ans_digraph.add_edges_from(ans_edge)
pos2 = {n:(2, 2-(i/2)) for i, n in enumerate(ans_digraph.nodes)}
nx.draw_networkx(ans_digraph,pos2,node_color="darkorange",node_size=1000,with_labels=True)
plt.savefig('digraph_sample2.png')
plt.show()

from Graph import *

#オイラーグラフ?
def Is_Eulerian_Graph(G: Graph):
    """ グラフ G がオイラーグラフかどうかを判定する. """
    return all(G.degree(v) % 2 == 0 for v in range(G.order())) and Is_Connected(G)

#準オイラーグラフ?
def Is_Semi_Eulerian_Graph(G: Graph):
    """ グラフ G が準オイラーグラフかどうかを判定する. """
    return len([v for v in range(G.order()) if G.degree(v) % 2 == 0]) == 2 and Is_Connected(G)

#Euler 路を見つける
def Find_Eulerian_Trail(G: Graph):
    pass

#Euler閉路を見つける
def Find_Eulerian_Cycle(G: Graph):
    pass
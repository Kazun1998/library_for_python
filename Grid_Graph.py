"""注意:
(1) 全て0-index
(2) x座標正が下, y座標正が右
"""

def Position_to_Number(x,y,H,W):
    return x*W+y

def Number_to_Position(p,H,W):
    return divmod(p,W)

def Position_Neighborhood(x,y,H,W):
    B=[]
    for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=x+a<H and 0<=y+b<W:
            B.append((x+a,y+b))
    return B

def Number_Neighborhood(p,H,W):
    B=[]
    if 0<=p-W:
        B.append(p-W)
    if p+W<H*W:
        B.append(p+W)
    if p%W:
        B.append(p-1)
    if (p+1)%W:
        B.append(p+1)
    return B

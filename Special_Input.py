##と.で表されたグリッドを01に変換する.
def Black_White_Grid(H: int, W: int, wall=False):
    """H: 縦のマス数, W: 横のマス数

    ※通れるところが1
    """

    f=lambda s:1 if s=="." else 0

    if wall:
        S=[[0]*(W+2)]
    else:
        S=[]

    for _ in range(H):
        if wall:
            S.append([0]+list(map(f,input()))+[0])
        else:
            S.append(list(map(f,input())))

    if wall:
        S.append([0]*(W+2))

    return S

#小数点以下第 k 位まで与えられる小数を 10^k 倍する.
def Decimal_to_Int(s: str, k: int, base=10) -> int:
    """ s*10^k を整数で出力する.

    s: 小数点を含むかもしれない数
    k: 小数点以下高々何位までか?
    base: 基数 (大体 10)
    """

    if "." not in s:
        return int(s,base)*pow(base,k)

    m=s.index(".")
    return int(s.replace(".",""))*pow(base,k-(len(s)-m-1))

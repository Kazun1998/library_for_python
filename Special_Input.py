##と.で表されたグリッドを01に変換する.
def Black_White_Grid(H:int,W:int) -> list:
    """H:縦のマス数, W:横のマス数
    """

    f=lambda s:1 if s=="#" else 0
    S=[]
    for _ in range(H):
        T=input()
        assert len(T)==W
        S.append(list(map(f,T)))
    return S

#小数点以下第k位まで与えられる小数を10^k倍する.
def Decimal_to_Int(s:str,k:int,base=10) -> int:
    """

    s:小数点を含むかもしれない数
    k:小数点以下高々何位までか?
    base:基数
    """

    if "." not in s:
        return int(s,base)*pow(base,k)

    m=s.index(".")
    return int(s.replace(".",""))*pow(base,k-(len(s)-m-1))

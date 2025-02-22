from typing import TypeVar, Generic, Callable, Iterator

M = TypeVar('M')
class Segment_Tree(Generic[M]):
    def __init__(self, L: list[M], op: Callable[[M, M], M], unit: M):
        """ op を演算とする初期状態 L の Segment Tree を生成する.

        Args:
            L (list[M]): 初期状態
            op (Callable[[M, M], M]): 演算
            unit (M): M の単位元
        """
        self.op=op
        self.unit=unit

        N=len(L); self.n=N
        d=max(1,(N-1).bit_length())
        k=1<<d

        self.data=data=[unit]*k+L+[unit]*(k-len(L))
        self.N=k
        self.depth=d

        for i in range(k-1,0,-1):
            data[i]=op(data[i<<1], data[i<<1|1])

    def get(self, k: int) -> M:
        """ 第 k 要素を取得する.

        Args:
            k (int): 要素の場所

        Returns:
            M: 第 k 要素
        """
        assert 0<=k<self.N,"添字が範囲外"
        return self.data[k+self.N]

    def update(self, k: int, x: M) -> None:
        """ 第 k 要素を x に変え, 更新する.

        Args:
            k (int): 要素の場所
            x (M): 更新後の第 k 要素
        """

        assert 0<=k<self.N,"添字が範囲外"
        m=k+self.N

        data=self.data; op=self.op
        data[m]=x

        while m>1:
            m>>=1
            data[m]=op(data[m<<1], data[m<<1|1])

    def product(self, l: int, r: int, left_closed: bool = True, right_closed: bool = True) -> M:
        """ 第 l 要素から第 r 要素までの総積を求める.

        Args:
            l (int): 左端
            r (int): 右端
            left_closed (bool, optional): False にすると, 左端が開区間になる. Defaults to True.
            right_closed (bool, optional): False にすると, 右端が開区間になる. Defaults to True.

        Returns:
            M: 第 l 要素から第 r 要素までの積
        """

        L=l+self.N+(not left_closed)
        R=r+self.N+(right_closed)

        vL=self.unit
        vR=self.unit

        data=self.data; op=self.op
        while L<R:
            if L&1:
                vL=op(vL, data[L])
                L+=1

            if R&1:
                R-=1
                vR=op(data[R], vR)

            L>>=1
            R>>=1

        return op(vL,vR)

    def all_product(self) -> M:
        return self.data[1]

    def max_right(self, left: int, cond: Callable[[int], bool]) -> int:
        """ 以下の2つをともに満たす r の1つを返す.\n
        (1) r=left or cond(data[left]*data[left+1]*...*data[r-1]): True\n
        (2) r=N or cond(data[left]*data[left+1]*...*data[r]): False\n

        ※ cond が単調減少の時, cond(data[left]*...*data[r-1]) を満たす最大の r となる.\n
        ※ cond(unit) = True を課す.

        Args:
            left (int): 左端
            cond (Callable[[int], bool]): 条件

        Returns:
            int: r
        """

        assert 0<=left<=self.N,"添字が範囲外"
        assert cond(self.unit),"単位元が条件を満たさない."

        if left==self.N:
            return self.N

        left+=self.N
        sm=self.unit

        op=self.op; data=self.data
        first=True

        while first or (left & (-left))!=left:
            first=False
            while left%2==0:
                left>>=1
            if not cond(op(sm, data[left])):
                while left<self.N:
                    left<<=1
                    if cond(op(sm, data[left])):
                        sm=op(sm, data[left])
                        left+=1
                return left-self.N
            sm=op(sm, data[left])
            left+=1
        return self.N

    def min_left(self, right: int, cond: Callable[[int], bool]) -> int:
        """ 以下の 2 つをともに満たす l の1つを返す.\n
        (1) l=right or cond(data[l]*data[l+1]*...*data[right-1]): True\n
        (2) l=0 or cond(data[l-1]*data[l]*...*data[right-1]): False\n

        ※ cond が単調増加の時, cond(data[l]*...*data[right-1]) を満たす最小の l となる.\n
        ※ cond(unit) = True を課す.

        Args:
            right (int): 右端
            cond (Callable[[int], bool]): 条件

        Returns:
            int: l
        """

        assert 0<=right<=self.N,"添字が範囲外"
        assert cond(self.unit),"単位元が条件を満たさない."

        if right==0:
            return 0

        right+=self.N
        sm=self.unit

        op=self.op; data=self.data
        first=1
        while first or (right & (-right))!=right:
            first=0
            right-=1
            while right>1 and right&1:
                right>>=1

            if not cond(op(data[right], sm)):
                while right<self.N:
                    right=2*right+1
                    if cond(op(data[right], sm)):
                        sm=op(data[right], sm)
                        right-=1
                return right+1-self.N
            sm=op(data[right], sm)
        return 0

    def __getitem__(self, k: int) -> M:
        return self.get(k)

    def __setitem__(self, k: int, x: M) -> None:
        return self.update(k,x)

    def __iter__(self) -> Iterator[M]:
        for i in range(self.n):
            yield self.get(i)

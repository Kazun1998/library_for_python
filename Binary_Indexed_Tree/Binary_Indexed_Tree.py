from typing import TypeVar, Generic, Callable, Generator

Group = TypeVar('Group')
class Binary_Indexed_Tree(Generic[Group]):
    def __init__(self, L: list[Group], op: Callable[[Group, Group], Group], zero: Group, neg: Callable[[Group], Group]):
        """ op を群 Group の演算として L から Binary Indexed Tree を生成する.

        Args:
            L (list[Group]): 初期状態
            op (Callable[[Group, Group], Group]): 群演算
            zero (Group): 群 Group における単位元 (任意の x in Group に対して, x + e = e + x = x となる e in Group)
            neg (Callable[[Group], Group]): x in Group における逆元 (x + y = y + x = e となる y) を求める関数
        """

        self.op=op
        self.zero=zero
        self.neg=neg
        self.sub: Callable[[Group, Group], Group] = lambda x, y: self.op(x, self.neg(y))
        self.N=N=len(L)
        self.log=N.bit_length()-1

        X=[zero]*(N+1)

        for i in range(N):
            p=i+1
            X[p]=op(X[p],L[i])
            q=p+(p&(-p))
            if q<=N:
                X[q]=op(X[q], X[p])
        self.data=X

    def get(self, k: int) -> Group:
        """ 第 k 項を求める.

        Args:
            k (int): 要素の位置

        Returns:
            Group: 第 k 項
        """
        return self.sum(k, k)

    def add(self, k: int, x: Group) -> None:
        """ 第 k 項に x を加え, 更新する.

        Args:
            k (int): 要素の位置
            x (Group): 加える Group の要素
        """

        data=self.data; op=self.op
        p=k+1
        while p<=self.N:
            data[p]=op(self.data[p], x)
            p+=p&(-p)

    def update(self, k: int, x: Group) -> None:
        """ 第 k 項を x に変えて更新する.

        Args:
            k (int): 要素の位置
            x (Group): 更新先の値
        """

        a=self.get(k)
        y = self.sub(x, a)

        self.add(k,y)

    def sum(self, l: int, r: int) -> Group:
        """ 第 l 項から第 r 項までの総和を求める (ただし, l != 0 のときは Group が群でなくてはならない).

        Args:
            l (int): 左端
            r (int): 右端

        Returns:
            Group: 総和
        """

        l=l+1 if 0<=l else 1
        r=r+1 if r<self.N else self.N

        if l>r:
            return self.zero
        elif l==1:
            return self.__section(r)
        else:
            return self.sub(self.__section(r), self.__section(l - 1))

    def __section(self, x: int) -> Group:
        """ B[0] + B[1] + ... + B[x] を求める.

        Args:
            x (int): 右端

        Returns:
            Group: 総和
        """

        data=self.data; op=self.op
        S=self.zero
        while x>0:
            S=op(data[x], S)
            x-=x&(-x)
        return S

    def all_sum(self) -> Group:
        """ B[0] + B[1] + ... + B[len(B) - 1] を求める.

        Returns:
            Group: 総和
        """
        return self.sum(0, self.N-1)

    def binary_search(self, cond: Callable[[Group], bool]) -> int:
        """ cond(B[0] + B[1] + ... + B[k]) が True になる最小の k を止める.

        ※ Group は順序群である必要がある.
        ※ cond(zero) = True のとき, 返り値は -1 とする.
        ※ cond(B[0] + ... + B[k]) なる k が (0 <= k < N に) 存在しない場合, 返り値は N とする.

        Args:
            cond (Callable[[Group], bool]): 単調増加な条件

        Returns:
            int: cond(B[0] + B[1] + ... + B[k]) が True になる最小の k
        """

        if cond(self.zero):
            return -1

        j=0
        t=1<<self.log
        data=self.data; op=self.op
        alpha=self.zero

        while t>0:
            if j+t<=self.N:
                beta=op(alpha, data[j+t])
                if not cond(beta):
                    alpha=beta
                    j+=t
            t>>=1

        return j

    def __getitem__(self, index) -> Group:
        if isinstance(index, int):
            return self.get(index)
        else:
            return [self.get(t) for t in index]

    def __setitem__(self, index: int, val: Group):
        self.update(index, val)

    def __iter__(self):
        for k in range(self.N):
            yield self.sum(k, k)

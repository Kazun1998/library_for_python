class Slide_Product():
    """M項の積をスライドさせながらもとめる.
    """

    def __init__(self,M,calc,unit,inv):
        """スライド積クラスを生成する.

        M:項数, calc:2項演算, unit:単位元, inv:逆元
        ※calcについて, 左から新しい項を加えること.
        """
        from collections import deque
        self.M=M
        self.unit=unit
        self.calc=calc
        self.inv=inv
        self.queue=deque([unit]*M)

        self.prod=unit

    def push(self,x,k=1):
        """xをk回分pushする.

        x:value
        k:回数
        """
        k=min(self.M,k)
        while k>0:
            k-=1
            a=self.queue.popleft()
            self.queue.append(x)
            self.prod=self.calc(x,self.calc(self.prod,self.inv(a)))

    def push_pop(self,x):
        """xを1回pushし, 代わりにpopされたものを返す.

        x:value
        """
        a=self.queue.popleft()
        self.queue.append(x)
        self.prod=self.calc(x,self.calc(self.prod,self.inv(a)))
        return a

    def product(self):
        return self.prod

    def refresh(self):
        self.prod=self.unit
        for x in self.queue:
            self.prod=self.calc(x,self.prod)

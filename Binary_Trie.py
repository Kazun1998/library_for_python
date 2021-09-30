class Binary_Trie:
    """ Reference
    https://judge.yosupo.jp/submission/35057
    https://judge.yosupo.jp/submission/53782
    """

    def __init__(self, max_value, allow_multiple=False, query_number=None):
        self.bit=max_value.bit_length()
        self.upper=1<<self.bit
        self.multi=allow_multiple

        if query_number!=None:
            self.arc=[-1]*2*self.bit*query_number
            self.size=[0]*self.bit*query_number
            self.terminal=[0]*self.bit*query_number
            self.id=0
        else:
            self.arc=[-1,-1]
            self.size=[0]
            self.terminal=[0]

        self.query_number=query_number
        self.v_list=[0]*(self.bit+1)
        self.lazy_xor=0

    def xor_all(self, x):
        assert 0<=x<self.upper
        self.lazy_xor^=x

    def __ixor__(self, x):
        self.xor_all(x)
        return self

    def insert(self, x):
        """ x を追加する. """

        assert 0<=x<self.upper

        x^=self.lazy_xor
        v=0
        for i in reversed(range(self.bit)):
            d=(x>>i)&1
            if self.arc[2*v+d]==-1:
                if self.query_number!=None:
                    self.id+=1
                    self.arc[2*v+d]=self.id
                else:
                    self.arc[2*v+d]=len(self.size)
                    self.arc.append(-1); self.arc.append(-1)
                    self.terminal.append(0)
                    self.size.append(0)

            v=self.arc[2*v+d]
            self.v_list[i]=v

        if self.multi or self.terminal[v]==0:
            self.terminal[v]+=1
            for w in self.v_list:
                self.size[w]+=1

    def discard(self, x):
        """ x が存在する場合, x を削除する. """

        if not (0<=x<self.upper):
            return

        x^=self.lazy_xor
        v=0
        for i in reversed(range(self.bit)):
            d=(x>>i)&1
            if self.arc[2*v+d]==-1:
                return

            v=self.arc[2*v+d]
            self.v_list[i]=v

        if self.terminal[v]>0:
            self.terminal[v]-=1
            for w in self.v_list:
                self.size[w]-=1

    def erase(self, x, k):
        """ x を高々 k 回削除する (ただし, k=-1 のときは無限回)"""

        assert -1<=k
        if not (0<=x<self.upper):
            return

        x^=self.lazy_xor
        v=0
        for i in reversed(range(self.bit)):
            d=(x>>i)&1
            if self.arc[2*v+d]==-1:
                return

            v=self.arc[2*v+d]
            self.v_list[i]=v

        if (k==-1) or (self.terminal[v]<k):
            k=self.terminal[v]

        if self.terminal[v]>0:
            self.terminal[v]-=k
            for w in self.v_list:
                self.size[w]-=k

    def count(self, x):
        """ x の個数を求める. """
        if not (0<=x<self.upper):
            return 0

        x^=self.lazy_xor
        v=0
        for i in reversed(range(self.bit)):
            d=(x>>i)&1
            if self.arc[2*v+d]==-1:
                return 0
            v=self.arc[2*v+d]
        return self.terminal[v]

    def __contains__(self, x):
        return bool(self.count(x))

    def __len__(self):
        return self.size[0]

    def __bool__(self):
        return bool(len(self))

    def less_count(self, x, equal=False):
        """ x 未満の要素数を求める (equal=True のときは, "未満" が "以下" になる)"""

        x^=self.lazy_xor
        if equal:
            x+=1

        if x<0:
            return 0

        if self.upper<=x:
            return len(self)

        v=0
        res=0
        for i in reversed(range(self.bit)):
            d=(x>>i)&1
            lc=self.arc[2*v]
            rc=self.arc[2*v+1]

            if (self.lazy_xor>>i)&1:
                lc,rc=rc,lc

            if d:
                if lc!=-1:
                    res+=self.size[lc]
                if rc==-1:
                    return res
                v=rc
            else:
                if lc==-1:
                    return res
                v=lc
        return res

    def more_count(self, x, equal=False):
        """ x より大きい要素数を求める (equal=True のときは, "より大きい" が "以上" になる)"""

        return len(self)-self.less_count(x,not equal)

    def low_value(self, x, equal=False, default=None):
        """ x 未満の整数のうち, 最大の整数を求める (存在しない場合は default).

        equal: True のとき, "未満" が "以下" になる.
        """

        x^=self.lazy_xor
        if equal:
            x+=1

        alpha=self.less_count(x,False)
        if alpha==0:
            return default
        else:
            return self.kth_element(alpha,1)

    def high_value(self, x, equal=False, default=None):
        """ x より大きい整数のうち, 最小の整数を求める (存在しない場合は default)

        equal: True のとき, "より大きい" が "以上" になる.
        """

        x^=self.lazy_xor
        if equal:
            x-=1

        beta=self.more_count(x,False)
        if beta==0:
            return default
        else:
            return self.kth_element(-beta,0)

    def kth_element(self, k, index=0):
        """ index -indexed で k 番目に小さい値を求める.
        ただし, index=0, k<0 のときは |k| 番目に大きい値になる.

        """

        if k<0:
            k+=self.size[0]
        k-=index
        assert 0<=k<self.size[0]

        v=0
        res=0
        for i in reversed(range(self.bit)):
            lc=self.arc[2*v]
            rc=self.arc[2*v+1]

            if (self.lazy_xor>>i)&1:
                lc,rc=rc,lc

            if lc==-1:
                v=rc
                res|=1<<i
            elif self.size[lc]<=k:
                k-=self.size[lc]
                v=rc
                res|=1<<i
            else:
                v=lc
        return res

    def get_min(self):
        return self.kth_element(1,1)

    def get_max(self):
        return self.kth_element(-1)

    def get_median(self, mode=0, func=None):
        """ 中央値を求める.

        [mode] 項の数が偶数のときの中央値の求め方を指定する (その 2値を a,b (a<=b) とする).
        mode=-1 → a
        mode= 0 → (a+b)/2 (float 型)
        mode= 1 → b
        mode=(その他) → その他 ( 2変数関数 func(a,b) で指定)
        """

        if len(self)%2==1:
            return self.kth_element(len(self)//2)
        else:
            a=self.kth_element(len(self)//2)
            b=self.kth_element(len(self)//2-1)

            if mode==-1:
                return a
            elif mode==1:
                return b
            elif mode==0:
                return (a+b)/2
            else:
                return func(a,b)

    def __getitem__(self, index):
        return self.kth_element(index)

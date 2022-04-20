class Fully_Indexable_Dictionary:
    """
    references:
    https://judge.yosupo.jp/submission/33990
    """
    def __init__(self, N):
        """ 長さ N の完備辞書生成する.

        """

        self.N=N
        self.blocks=(N+31)>>5
        self.bit=[0]*self.blocks
        self.total=[0]*self.blocks
        self.mask=[(1<<i)-1 for i in range(1<<5)]

    def __popcount(self, x):
        x = x - ((x >> 1) & 0x55555555)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = x + (x >> 4) & 0x0f0f0f0f
        x = x + (x >> 8)
        x = x + (x >> 16)
        return x & 0x0000007f

    def __len__(self):
        return self.N

    def set(self, index, bit):
        """ 第 index 要素を bit に設定する.

        """
        if index<0:
            index+=self.N

        if bit:
            self.bit[index>>5]|=1<<(index&31)
        else:
            self.bit[index>>5]|=~(1<<(index&31))

    def build(self):
        """ データ構造を確定させる. ※ 以降, set の使用禁止

        """

        for k in range(1, self.blocks):
            self.total[k]=self.total[k-1]+self.__popcount(self.bit[k-1])

    def access(self, index):
        """ 第 index 要素の値を求める.

        """
        if index<0:
            index+=self.N

        return (self.bit[index>>5]>>(index&31))&1

    __getitem__=access

    def rank(self, index, bit):
        """ [0, index) にある bit の数を求める.

        """
        if index<=0:
            return 0

        index=min(index, self.N)

        if index<self.N:
            alpha=self.total[index>>5]+self.__popcount(self.bit[index>>5]&self.mask[index&31])
        else:
            alpha=self.total[-1]+self.__popcount(self.bit[-1])
        return alpha if bit else index-alpha

    def  select(self, k, bit, default=-1):
        """ 先頭から k (1-indexed) 番目の bit の位置を求める.

        """
        if (k<1 or self.rank(self.N, bit)<k):
            return default

        l,r=0,self.N
        while r-l>1:
            m=(l+r)//2
            if self.rank(m, bit)>=k:
                r=m
            else:
                l=m
        return l

class Wavelet_Matrix:
    def __init__(self, X):
        """ X についての Wavelet 行列を作成する.

        """

        self.N=N=len(X)

        self.value_list=sorted(set(X))
        self.value_dict={x:i for i,x in enumerate(self.value_list)}
        Y=[self.value_dict[x] for x in X]

        self.bit_size=len(self.value_dict).bit_length()
        self.max_value=(1<<self.bit_size)-1

        self.zero_count=[0]*self.bit_size
        self.dict=[Fully_Indexable_Dictionary(N) for _ in range(self.bit_size)]

        for lv in range(self.bit_size-1,-1,-1):
            dic=self.dict[~lv]
            left=[]; right=[]
            for i in range(N):
                if (Y[i]>>lv)&1:
                    dic.set(i,1)
                    right.append(Y[i])
                else:
                    left.append(Y[i])

            dic.build()
            self.zero_count[~lv]=len(left)

            Y=left+right

        self.begin=[0]*len(self.value_dict)
        for i in range(N-1,-1,-1):
            self.begin[Y[i]]=i

    def access(self, index):
        """ index 番目の要素を求める.

        index: 番号
        """

        if index<0:
            index+=self.N

        p=0
        for lv in range(self.bit_size):
            dic=self.dict[lv]
            bit=dic.access(index)
            p=(p<<1)|bit

            if bit:
                index=self.zero_count[lv]+dic.rank(index, 1)
            else:
                index=dic.rank(index,0)
        return self.value_list[p]

    __getitem__=access

    def __len__(self):
        return self.N

    def rank(self, i, value):
        """ [0,i) にある value の個数を求める.

        i: 右端 (第 i 要素を含まない)
        value: 値
        """
        return self.range_rank(0,i,value)

    def range_rank(self, l, r, value):
        """ [l,r) にある value の個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        value=self.value_dict.get(value,-1)
        if value==-1:
            return 0

        for lv in range(self.bit_size):
            dic=self.dict[lv]
            if (value>>(self.bit_size-lv-1))&1:
                l=dic.rank(l,1)+self.zero_count[lv]
                r=dic.rank(r,1)+self.zero_count[lv]
            else:
                l=dic.rank(l,0)
                r=dic.rank(r,0)

        return r-l

    def select(self, value, k, default=-1):
        """ k (1-indexed) 番目に登場する value の位置を求める.
        """

        value=self.value_dict.get(value,-1)
        if value==-1:
            return default

        p=self.begin[value]
        index=p+k-1

        for lv in range(self.bit_size):
            dic=self.dict[~lv]
            if (value>>lv)&1:
                index=dic.select(index-self.zero_count[~lv]+1, 1, default)
            else:
                index=dic.select(index+1, 0, default)

            if index==default:
                return default
        return index

    def quantile(self, l, r, k):
        """ [l,r) における k (1-indexed) 番目に小さい値を求める.
        """

        p=0
        for lv in range(self.bit_size):
            dic=self.dict[lv]
            alpha=dic.rank(r,0)-dic.rank(l,0)
            p<<=1
            if alpha<k:
                p|=1
                k-=alpha
                l=dic.rank(l,1)+self.zero_count[lv]
                r=dic.rank(r,1)+self.zero_count[lv]
            else:
                l=dic.rank(l,0)
                r=dic.rank(r,0)
        return self.value_list[p]

    kth_min=quantile

    def kth_max(self, l, r, k):
        return self.quantile(l,r,r-l-k+1)

    def top(self, l, r, k):
        """ [l,r) にある出現回数が多い順から k 個 (値, 個数) のタプルを出力する (個数同率は値が小さい方が優先).

        l: 左端
        r: 右端 (第 r 項を含まない)
        k: 採用する要素数
        """

        assert k>=1

        from heapq import heappush, heappop
        X=[]
        Q=[(-(r-l), 0, 0, l,r)]
        while k and Q:
            _,value,lv,l,r=heappop(Q)

            if lv==self.bit_size:
                X.append((self.value_list[value], r-l))
                k-=1
            else:
                dic=self.dict[lv]
                beta=dic.rank(l,0)
                alpha=dic.rank(r,0)-beta

                # 0
                if alpha>0:
                    heappush(Q, (-alpha, value<<1, lv+1, beta, beta+alpha))

                # 1
                if (r-l)-alpha>0:
                    x=self.zero_count[lv]+(l-beta)
                    y=x+(r-l-alpha)
                    heappush(Q, (-((r-l)-alpha), (value<<1)|1, lv+1, x, y))
        return X

    def sum(self, l, r):
        X=0
        for x,f in self.top(l,r,r-l):
            X+=x*f
        return X

    def range_all(self, l, r, value):
        """ [l,r) にある (value 未満の個数, value ちょうどの個数, value より大きい個数) を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_freq(self, l, r, x, y):
        """ [l,r) にある x 以上 y 未満の個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_less(self, l, r, value):
        """ [l,r) にある value 未満の個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_more(self, l, r, value):
        """ [l,r) にある value より大きい個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """

        pass

    def range_list(self, l, r, a, b):
        """ [l,r) にある (value 未満の個数, value ちょうどの個数, value より大きい個数) を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        """
        pass

    def range_max(self, l, r, k):
        pass

    def range_min(self, l, r, k):
        pass

    def prev_value(self, l, r, a, b):
        pass

    def next_value(self, l, r, a, b):
        pass

    def intersect(self, l1, r1, l2, r2):
        """ [l1, r1), [l2, r2) に共に存在する要素 v における (v, 1番目の区間にある v  の個数, 2番目の区間にある v  の個数) のリストを出力する.

        """

        X=[(l1,r1,l2,r2,0)]
        for lv in range(self.bit_size):
            Y=X; X=[]
            dic=self.dict[lv]
            for l1,r1,l2,r2,value in Y:
                beta1=dic.rank(l1,0); alpha1=dic.rank(r1,0)-beta1
                a1=beta1; b1=beta1+alpha1
                c1=self.zero_count[lv]+(l1-beta1); d1=c1+(r1-l1-alpha1)

                beta2=dic.rank(l2,0); alpha2=dic.rank(r2,0)-beta2
                a2=beta2; b2=beta2+alpha2
                c2=self.zero_count[lv]+(l2-beta2); d2=c2+(r2-l2-alpha2)

                if a1<b1 and a2<b2:
                    X.append((a1,b1,a2,b2,value<<1))

                if c1<d1 and c2<d2:
                    X.append((c1,d1,c2,d2,(value<<1)|1))

        return [(self.value_list[value], y1-x1, y2-x2) for x1,y1,x2,y2,value in X]

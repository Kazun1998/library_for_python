class Binary_Indexed_Tree_Exception(Exception):
    pass

"""
Note:各群演算に関する関数と単位元
[和]
calc=lambda x,y:x+y
unit=0
[積]
calc=lambda x,y:x*y
unit=1
[Bit Or]
calc=lambda x,y:x|y
unit=0
[Bit And]
calc=lambda x,y:x&y
unit=(※任意の要素xでx<2**kが保証されているとき,単位元として2**k-1が取れる.)
[Bit Xor]
calc=lambda x,y:x^y
unit=0
[最小値]
calc=lambda x,y:min(x,y)
unit=float("inf")
[最大値]
calc=lambda x,y:max(x,y)
unit=-float("inf")
[集合の和]
calc=lambda x,y:x|y
unit=set()
[集合の積]
calc=lambda x,y:x&y
unit=(全体の集合(場合による))
[集合の対称差]
calc=lambda x,y:x^y
unit=set()
"""

class Binary_Indexed_Tree():
    def __init__(self,L,calc,unit,inv,index=1):
        """calcを演算とするN項のBinary Indexed Treeを作成
        calc:演算(2変数関数,群)
        unit:群calcの単位元(xe=ex=xを満たすe)
        inv:群calcの逆元(1変数関数)
        """
        self.calc=calc
        self.unit=unit
        self.inv=inv
        self.index=index

        N=len(L)
        d=max(1,(N-1).bit_length())
        k=2**d

        X=[None]+[unit]*k

        self.num=k
        self.depth=d

        if L:
            for i in range(len(L)):
                p=i+1
                while p<=k:
                    X[p]=self.calc(X[p],L[i])
                    p+=p&(-p)
        self.data=X

    def index_number(self,k,index=1):
        """第k要素の値を出力する.
        k:数列の要素
        index:先頭の要素の番号
        """
        return self.sum(k,k,index)

    def add(self,k,x,index=1,right=False):
        """第k要素にxを左から加え,更新を行う.
        k:数列の要素
        x:更新後の値
        index:先頭の要素の番号
        right:「左から」が「右から」になる
        """
        p=k+(1-index)
        while p<=self.num:
            if right==False:
                #左から
                self.data[p]=self.calc(x,self.data[p])
            else:
                #右から
                self.data[p]=self.calc(self.data[p],x)
            p+=p&(-p)

    def update(self,k,x,index=1,right=False):
        """第k要素をxに変え,更新を行う.
        k:数列の要素
        x:更新後の値
        """

        a=self.index_number(k,index)
        if right==False:
            #左から
            y=self.calc(x,self.inv(a))
        else:
            #右から
            y=self.calc(self.inv(a),x)

        self.add(k,y,index,right)

    def sum(self,From,To,index=1):
        """第From要素から第To要素までの総和を求める.
        ※From!=1を使うならば,群でなくてはならない.
        From:始まり
        To:終わり
        index:先頭の要素の番号
        """
        alpha=max(1,From+(1-index))
        beta=min(self.num,To+(1-index))

        if alpha==1:
            return self.__section(beta)
        else:
            return self.calc(self.inv(self.__section(alpha-1)),self.__section(beta))

    def __section(self,To):
        S=self.unit
        x=To
        while x>0:
            S=self.calc(self.data[x],S)
            x-=x&(-x)
        return S

    def all_sum(self):
        return self.data[-1]

    def __getitem__(self,index):
        if isinstance(index,int):
            return self.index_number(index,self.index)
        else:
            return [self.index_number(t,self.index) for t in index]

    def __setitem__(self,index,val):
        self.update(index,val,self.index)
from Double_Heap import *

class Median:
    def __init__(self):
        self.left=Double_Heap()
        self.right=Double_Heap()

    def __bool__(self):
        return bool(self.left) or bool(self.right)

    def __len__(self):
        return len(self.left)+len(self.right)

    def __contains__(self, x):
        return (x in self.left) or (x in self.right)

    def push(self, x):
        """ 要素 x を追加する. """

        if len(self.left)==len(self.right):
            u=self.right.get_min() if self.right else float("inf")
            if x>u:
                v=self.right.pop_min()
                self.left.push(v)
                self.right.push(x)
            else:
                self.left.push(x)
        else:
            u=self.left.get_max()
            if x>u:
                self.right.push(x)
            else:
                v=self.left.pop_max()
                self.left.push(x)
                self.right.push(v)

    def erase(self,x):
        """ 要素 x を削除する. """

        assert x in self
        alpha=self.left.get_max() if self.left else -float("inf")
        if len(self.left)==len(self.right):
            if x<=alpha:
                self.left.discard(x)
                y=self.right.pop_min()
                self.left.push(y)
            else:
                self.right.discard(x)
        else:
            if x<=alpha:
                self.left.discard(x)
            else:
                self.right.discard(x)
                y=self.left.pop_max()
                self.right.push(y)

    def get_median(self,mode=0,func=None):
        """ 中央値を求める.

        [mode] 項の数が偶数のときの中央値の求め方を指定する (その 2値を a,b (a<=b) とする).
        mode=-1 → a
        mode=0  → (a+b)/2
        mode=1 → b
        mode=(その他) → その他 ( 2変数関数 func(a,b) で指定)
        """

        assert self, "キューが空です"

        if len(self)%2==1:
            return self.left.get_max()
        else:
            if mode==-1:
                return self.left.get_max()
            elif mode==1:
                return self.right.get_min()
            else:
                a=self.left.get_max()
                b=self.right.get_min()

                if mode==0:
                    return (a+b)/2
                else:
                    return func(a,b)

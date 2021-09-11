import heapq

"""参考元
https://tsubo.hatenablog.jp/entry/2020/06/15/124657
"""

class Heap_Dict:
    def __init__(self, Mode=True):
        """

        Mode: True → 最小値, False → 最大値
        """
        self.heap=[]
        self.dict={}
        self.Mode=Mode
        self.__length=0

    def __bool__(self):
        return bool(self.heap)

    def __len__(self):
        return self.__length

    def __contains__(self, x):
        return self.is_exist(x)

    def insert(self, x):
        """ 要素 x を追加する. """

        if self.Mode and not self.is_exist(x):
            heapq.heappush(self.heap,x)
        elif not self.Mode and not self.is_exist(x):
            heapq.heappush(self.heap,-x)

        if x in self.dict:
            self.dict[x]+=1
        else:
            self.dict[x]=1

        self.__length+=1

    def erase(self, x):
        """ x を消す. """

        assert (x in self.dict) and (self.dict[x])

        self.dict[x]-=1
        self.__length-=1
        while self.heap:
            y=self.heap[0]
            if not self.Mode:y=-y
            if self.dict[y]==0:
                heapq.heappop(self.heap)
            else:
                break

    def is_exist(self, x):
        """ キューに x が存在するかどうかを判定する. """

        return (x in self.dict) and (self.dict[x])

    def get_min(self):
        """ キューにある最小値を返す.
        ※ Mode=True でないと使えない.

        """

        assert self.Mode

        if self.heap:
            return self.heap[0]
        else:
            return float("inf")

    def pop_min(self):
        """ キューにある最小値を取り出す.
        ※ Mode=True でないと使えない.

        """

        assert self.Mode

        x=self.get_min()
        self.erase(x)
        return x
         
    def get_max(self):
        """ キューにある最大値を返す.
        ※ Mode=False でないと使えない.

        """

        assert not self.Mode

        if self.heap:
            return -self.heap[0]
        else:
            return -float("inf")

    def pop_max(self):
        """ キューにある最小値を取り出す.
        ※ Mode = False でないと使えない.

        """

        assert not self.Mode

        x=self.get_max()
        self.erase(x)
        return x

    def count(self, x):
        """ x の個数を求める. """

        if x not in self.dict:
            return 0
        else:
            return self.dict[x]

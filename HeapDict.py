"""参考元
https://tsubo.hatenablog.jp/entry/2020/06/15/124657
"""
import heapq
class Heap_Dict:
    def __init__(self, mode=True):
        """ Heap Dict クラスの作成.

        Mode: True → 最小値, False → 最大値
        """
        self.heap=[]
        self.dict={}
        self.__mode=bool(mode)
        self.__length=0

    def __bool__(self):
        return bool(self.heap)

    def __len__(self):
        return self.__length

    def __contains__(self, x):
        return self.is_exist(x)

    def insert(self, x):
        """ 要素 x を追加する. """

        if self.__mode and not self.is_exist(x):
            heapq.heappush(self.heap,x)
        elif not self.__mode and not self.is_exist(x):
            heapq.heappush(self.heap,-x)

        if x in self.dict:
            self.dict[x]+=1
        else:
            self.dict[x]=1

        self.__length+=1

    def erase(self, x):
        """ x を消す (存在しない場合は KeyError) . """

        if x not in self:
            raise KeyError(x)

        self.dict[x]-=1
        self.__length-=1
        while self.heap:
            y=self.heap[0]
            if not self.__mode:y=-y
            if self.dict[y]==0:
                heapq.heappop(self.heap)
            else:
                break

    def discard(self, x):
        """ x を消す (存在しない場合は何もしない). """

        if x not in self:
            return

        self.dict[x]-=1
        self.__length-=1
        while self.heap:
            y=self.heap[0]
            if not self.__mode:y=-y
            if self.dict[y]==0:
                heapq.heappop(self.heap)
            else:
                break

    def is_exist(self, x):
        """ キューに x が存在するかどうかを判定する. """

        return bool(self.dict.get(x,0))

    def get_min(self, default=float("inf")):
        """ キューにある最小値を返す.
        ※ Mode=True でないと使えない.

        """

        assert self.__mode

        if self.heap:
            return self.heap[0]
        else:
            return default

    def pop_min(self):
        """ キューにある最小値を取り出す.
        ※ Mode=True でないと使えない.

        """

        assert self.__mode and bool(self)

        x=self.get_min()
        self.erase(x)
        return x

    def get_max(self, default=-float("inf")):
        """ キューにある最大値を返す.
        ※ Mode=False でないと使えない.

        """

        assert not self.__mode

        if self.heap:
            return -self.heap[0]
        else:
            return default

    def pop_max(self):
        """ キューにある最小値を取り出す.
        ※ Mode = False でないと使えない.

        """

        assert (not self.__mode) and bool(self)

        x=self.get_max()
        self.erase(x)
        return x

    def count(self, x):
        """ x の個数を求める. """

        return self.dict.get(x,0)

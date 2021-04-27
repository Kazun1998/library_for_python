import heapq

"""参考元
https://tsubo.hatenablog.jp/entry/2020/06/15/124657
"""

class Heap_Dict:
    def __init__(self,Mode=True):
        """

        Mode:True→最小値,False→最大値
        """
        self.heap=[]
        self.dict={}
        self.Mode=Mode

    def __bool__(self):
        return bool(self.heap)

    def insert(self,x):
        if self.Mode and not self.is_exist(x):
            heapq.heappush(self.heap,x)
        elif not self.Mode and not self.is_exist(x):
            heapq.heappush(self.heap,-x)

        if x in self.dict:
            self.dict[x]+=1
        else:
            self.dict[x]=1

    def erase(self,x):
        assert (x in self.dict) and (self.dict[x])

        self.dict[x]-=1

        while self.heap:
            y=self.heap[0]
            if not self.Mode:y=-y
            if self.dict[y]==0:
                heapq.heappop(self.heap)
            else:
                break

    def is_exist(self,x):
        return (x in self.dict) and (self.dict[x])

    def get_min(self):
        assert self.Mode

        if self.heap:
            return self.heap[0]
        else:
            return float("inf")

    def get_max(self):
        assert not self.Mode

        if self.heap:
            return -self.heap[0]
        else:
            return -float("inf")

    def count(self,x):
        if x not in self.dict:
            return 0
        else:
            return self.dict[x]

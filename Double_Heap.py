import heapq

class Double_Heap:
    def __init__(self):
        self.__small=[]
        self.__large=[]
        self.__dict={}
        self.__length=0
        self.__sum=0

    def __bool__(self):
        return bool(self.__length)

    def __len__(self):
        return self.__length

    def __contains__(self, x):
        return self.is_exist(x)

    def push(self, x):
        self.__length+=1
        self.__sum+=x

        heapq.heappush(self.__small, x)
        heapq.heappush(self.__large, -x)

        if x in self.__dict:
            self.__dict[x]+=1
        else:
            self.__dict[x]=1

    def discard(self, x):
        """ x を消す (存在しない場合は何もしない). """

        if x not in self:
            return

        self.__dict[x]-=1
        if self.__dict[x]==0:
            del self.__dict[x]

        self.__length-=1
        self.__sum-=x

        while self.__small and (self.__small[0] not in self):
                heapq.heappop(self.__small)

        while self.__large and (-self.__large[0] not in self):
                heapq.heappop(self.__large)

    def is_exist(self, x):
        """ キューに x が存在するかどうかを判定する. """
        return x in self.__dict

    def get_min(self):
        assert self
        return self.__small[0]

    def pop_min(self):
        assert self
        x=self.get_min()
        self.discard(x)
        return x

    def get_max(self):
        assert self
        return -self.__large[0]

    def pop_max(self):
        assert self
        x=self.get_max()
        self.discard(x)
        return x

    def count(self, x):
        """ x の個数を求める. """

        return self.__dict.get(x,0)

    def sum(self):
        return self.__sum

    def __str__(self):
        return str(self.__dict)

    def __repr__(self):
        return "[Double Heap]: "+str(self)

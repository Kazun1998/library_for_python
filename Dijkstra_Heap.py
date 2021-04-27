from heapq import heappop,heappush
class Heap_Point:
        def __init__(self,x,d):
            self.d=d
            self.x=x

        def __str__(self):
            return "(point:{}, dist:{})".format(self.x,self.d)

        def __repr__(self):
            return str(self)

        def __lt__(self,other):
            return self.d<other.d

        def __iter__(self):
            yield from (self.x,self.d)

class Dijkstra_Heap:
    def __init__(self):
        self.heap=[]

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        return repr(self.heap)

    def __bool__(self):
        return bool(self.heap)

    def push(self,point,dist):
        heappush(self.heap,Heap_Point(point,dist))

    def pop(self):
        assert self.heap
        return heappop(self.heap)

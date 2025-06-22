from heapq import heappop, heappush

class Dijkstra_Point:
    __slots__ = ("__point", "__dist")

    def __init__(self, point: int, dist: int):
        self.__dist = dist
        self.__point = point

    @property
    def dist(self) -> int:
        return self.__dist

    @property
    def point(self) -> int:
        return self.__point

    def __str__(self) -> str:
        return f"(point: {self.point}, dist: {self.dist})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(point={self.point}, dist={self.dist})"

    def __lt__(self, other: "Dijkstra_Point") -> bool:
        return self.dist < other.dist

    def __iter__(self):
        yield from (self.point, self.dist)

class Dijkstra_Heap:
    def __init__(self):
        self.__heap: list[Dijkstra_Point] = []

    def __bool__(self) -> bool:
        return bool(self.heap)

    def push(self, point: int, dist: int):
        """ 頂点 point までの距離が dist である情報をヒープに追加する.

        Args:
            point (int): 頂点
            dist (int): 距離
        """

        heappush(self.__heap, Dijkstra_Point(point, dist))

    def pop(self) -> Dijkstra_Point:
        """ 次に確定させるべき頂点と距離の情報を pop する.

        Returns:
            Dijkstra_Point: 次に確定させるべき頂点と距離の情報
        """
        assert self.heap
        return heappop(self.__heap)

class Weighted_Arc:
    __slots__ = ('__id', '__source', '__target', '__weight')

    def __init__(self, id: int, source: int, target: int, weight: int):
        self.__id = id
        self.__source = source
        self.__target = target
        self.__weight = weight

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, source={self.source}, target={self.target}, weight={self.weight})"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def source(self) -> int:
        return self.__source

    @property
    def target(self) -> int:
        return self.__target

    @property
    def weight(self) -> int:
        return self.__weight

class Weighted_Digraph:
    #入力定義
    def __init__(self, N: int = 0, arc_offset: int = 0):
        """ N 頂点の重み付き有向グラフを生成する.

        Args:
            N (int, optional): 頂点数. Defaults to 0.
            arc_offset (int, optional): 弧番号の offset. Defaults to 0.
        """

        self.adjacent_out: list[list[Weighted_Arc]] = [[] for _ in range(N)] # 出近傍 (v が始点)
        self.arcs: list[Weighted_Arc] = [None] * arc_offset
        self.__arc_offset = arc_offset
        self.__infinity = 0

    # property

    # 頂点数
    @property
    def vertex_count(self) -> int:
        """ グラフの頂点数 (位数) を求める."""
        return len(self.adjacent_out)

    @property
    def order(self) -> int:
        """ グラフの位数 (頂点数) を求める."""
        return len(self.adjacent_out)

    #辺数
    @property
    def arc_count(self) -> int:
        """ グラフの辺数 (サイズ) を求める."""
        return len(self.arcs) - self.__arc_offset

    @property
    def size(self) -> int:
        """ グラフのサイズ (辺数) を求める. """
        return len(self.arcs) - len(self.__arc_offset)

    @property
    def inifinity(self) -> int:
        return self.__infinity

    @inifinity.setter
    def infinity(self, value):
        self.__infinity = value

    #頂点の追加
    def add_vertex(self) -> int:
        """ 頂点を 1 個追加して, その頂点の番号を返す.

        Returns:
            int: 追加した頂点の番号
        """

        self.adjacent_out.append([])
        return self.order - 1

    def add_vertices(self, k: int) -> list[int]:
        """ 頂点を k 個追加して, その頂点の番号を返す.

        Returns:
            list[int]: 追加した k 個の頂点の番号のリスト
        """

        return [self.add_vertex() for _ in range(k)]

    #辺の追加
    def add_arc(self, source: int, target: int, weight: int = 1) -> int:
        """ source から target へ結ぶ重み weight の弧を追加し, 弧の番号を出力する.

        Args:
            source (int): 始点
            target (int): 終点
            weight (int, optional): 重み. Defaults to 1.

        Returns:
            int: 追加した弧の番号
        """

        id = self.arc_count + self.__arc_offset
        arc = Weighted_Arc(id, source, target, weight)
        self.adjacent_out[source].append(arc)
        self.arcs.append(arc)
        self.__infinity += 2 * max(1, abs(weight))
        return id

    #近傍

    #出次数
    def out_degree(self, v: int) -> int:
        """ 頂点 v の出次数 (v を始点とする有向辺の数) を求める

        Args:
            v (int): 頂点

        Returns:
            int: 出次数
        """

        return len(self.adjacent_out[v])

    def initialize_list(self, x) -> list:
        return [x] * self.order

    def arcs_generator(self):
        for j in range(self.__arc_offset, self.__arc_offset + self.arc_count):
            yield self.arcs[j]

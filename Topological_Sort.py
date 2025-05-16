class Topological_Sort:
    __slots__=("__arc", "__rev", "__reflexive", "__is_DAG", "__order")

    def __init__(self, N: int, reflexive: bool = False):
        """ N 頂点からなる有向空グラフを生成する.

        Args:
            N (int): 頂点数
            reflexive (bool, optional): True にすると, 自己ループの追加を認める. Defaults to False.
        """

        self.__arc=[[] for _ in  range(N)]
        self.__rev=[[] for _ in range(N)]
        self.__reflexive=reflexive

    @property
    def N(self):
        return len(self.__arc)

    @property
    def reflexive(self):
        return self.__reflexive

    def add_arc(self, source: int, target: int):
        """ source から target への弧を追加する.

        Args:
            source (int): 始点
            target (int): 終点
        """

        # 自己ループを認めない場合の source == target のときは棄却する.
        if source == target and (not self.reflexive):
            return

        self.__arc[source].append(target)
        self.__rev[target].append(source)

    def add_vertex(self) -> int:
        """ 1 頂点追加

        Returns:
            int: 追加された頂点の頂点番号
        """

        self.__arc.append([])
        self.__rev.append([])
        return self.N - 1

    def add_arc_multiple(self, sources: list[int], targets: list[int]) -> int:
        """ 任意の s in sources, t in targets に対して, s から t への弧を作成する (仮想的に 1 頂点を追加する).

        Args:
            sources (list[int]): 始点のリスト
            targets (list[int]): 終点のリスト

        Returns:
            int: 超頂点として追加された頂点の番号
        """

        # 方針
        # (1) 超頂点 x を追加する.
        # (2) 任意の s in sources に対して, 弧 sx を追加する.
        # (3) 任意の t in targets に対して, 弧 xt を追加する.
        # このようにすることで, 追加する弧の数を |sources| x |targets| から |sources| + |targets| に落とせる.

        x = self.add_vertex()
        for s in sources:
            self.add_arc(s, x)

        for t in targets:
            self.add_arc(x, t)

    def calculate(self):
        """ DAG に関する計算を行う.
        """

        in_deg = [len(self.__rev[x]) for x in range(self.N)]
        order = []
        stack = [x for x in range(self.N) if in_deg[x] == 0]

        while stack:
            x = stack.pop()
            order.append(x)

            for y in self.__arc[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    stack.append(y)

        if len(order) == self.N:
            self.__is_DAG = True
            self.__order = order
        else:
            self.__is_DAG = False
            self.__order = None

    @property
    def is_DAG(self):
        return self.__is_DAG

    @property
    def order(self):
        return self.__order

from bisect import bisect_left

class Partial_Persistent_List:
    def __init__(self, A: list, auto_commit = False):
        """ リスト A を半永続リストにする.

        Args:
            A (list): 元となるリスト
            auto_commit (bool, optional): True ならば代入すると自動的に時刻が進み, False ならば時刻は self.forward_time() で進めなければならない. Defaults to False.
        """

        self.__N = N = len(A)
        self.__auto_commit = auto_commit

        self.__set_time = [[-1] for _ in range(N)]
        self.__set_value = [[a] for a in A]
        self.__time = 0

    @property
    def auto_commit(self) -> bool:
        return self.__auto_commit

    @property
    def get_time(self) -> int:
        return self.__time

    def get_value(self, index: int, time: int = -1):
        """ 時刻 time の第 index 要素を取得する.

        Args:
            index (int): 要素番号
            time (int, optional): 時刻. ただし, time = -1 にすると, 最新の第 index 要素を取得する. Defaults to -1.

        Returns:
            _type_: _description_
        """
        if time >= 0:
            j = bisect_left(self.__set_time[index], time) - 1
        else:
            j = len(self.__set_time[index]) - 1

        return self.__set_value[index][j]

    def set_value(self, index: int, value):
        """ 第 index 要素を value に変更する.

        Args:
            index (int): 要素番号
            value : 要素
        """

        times = self.__set_time[index]
        values = self.__set_value[index]

        if times[-1] == self.time:
            values[-1] = value
        else:
            times.append(self.time)
            values.append(value)

        if self.auto_commit:
            self.commit()

    def commit(self) -> int:
        """ 時刻を 1 つすすめる.

        Returns:
            int: 進めた後の時刻
        """

        self.__time += 1
        return self.time

    def __len__(self) -> int:
        return len(self.__set_value)

    def __str__(self):
        return str([self[i] for i in range(self.__N)])

    def __repr__(self):
        return f"{self.__class__.__name__}(A={repr([self[i] for i in range(len(self))])}, auto_commit={self.auto_commit})"

    def __iter__(self):
        for i in range(self.__N):
            yield self[i]

    def __setitem__(self, index, value):
        self.set_value(index, value)

    def __getitem__(self, index: int):
        return self.__set_value[index][-1]

from typing import TypeVar, Generic

class DuplicateValue(Exception):
    pass

T = TypeVar('T')
class Unique_List(Generic[T]):
    def __init__(self, A: list[T | None]):
        """ 要素の一意性が保証されたリストを生成する.

        Args:
            A (list[T]): 重複が存在しないリスト

        Raises:
            DuplicateValue: A に重複があったときに発生
        """

        index: dict[T, int] = {}
        for i, a in enumerate(A):
            if a is None:
                continue

            if a in index:
                raise DuplicateValue('重複する要素があります')

            index[a] = i

        self.__list = A
        self.__index = index

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__list})"

    def update(self, i: int, a: T):
        """ 第 i 要素を a に変更する (変更後に重複する要素があってはいけない)

        Args:
            i (int): 変更する場所
            a (T): 変更後の値

        Raises:
            DuplicateValue: (変更後に重複する要素があってはいけない)
        """

        # 変わらないならば早期 Return
        if self[i] == a:
            return

        # 重複チェック
        if a in self.__index:
            raise DuplicateValue

        del self.__index[self[i]]

        if a is not None:
            self.__index[a] = i

        self.__list[i] = a

    def __getitem__(self, i: int) -> T:
        return self.__list[i]

    __setitem__ = update

    def __include__(self, a: T) -> bool:
        return a in self.__index

    def index(self, a: T, default = None) -> int:
        """ a がある場所を取得する (存在しない場合は default)

        Args:
            a (T): 探索する要素
            default (_type_, optional): 存在しない場合の返り値. Defaults to None.

        Returns:
            int: a がある場所
        """

        return self.__index.get(a, default)

    def swap(self, i: int, j: int):
        """ 第 i 要素と第 j 要素を交換する.

        Args:
            i (int):
            j (int):
        """

        a = self.__list[i]; b = self.__list[j]

        self.__list[i] = b; self.__list[j] = a
        self.__index[a] = j; self.__index[b] = i

    def transposition(self, a: T, b: T):
        """ 要素 a と要素 b を交換する.

        Args:
            a (T):
            b (T):
        """

        i = self.__index[a]; j = self.__index[b]

        self.__list[i] = b; self.__list[j] = a
        self.__index[a] = j; self.__index[b] = i

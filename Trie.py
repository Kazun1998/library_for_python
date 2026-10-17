from typing import TypeVar, Iterable, Generic

T = TypeVar('T')
class Trie_Node(Generic[T]):
    __slots__ = ('_item', '_next', '_terminal_count', '_prefix_count')

    def __init__(self, item: T | None):
        self._item = item
        self._next: dict[T, "Trie_Node"] = {}
        self._terminal_count = 0
        self._prefix_count = 0

    def __str__(self):
        if self.terminal_count:
            return "({}) [{} ({})]: {}".format(self.terminal_count, self.item,self.prefix_count,self.next)
        else:
            return "[{} ({})]: {}".format(self.item,self.prefix_count,self.next)

    def __repr__(self):
        return f"{self.__class__.__name__}(item={self.item})"

    @property
    def item(self):
        return self._item

    @property
    def next(self):
        return self._next

    @property
    def terminal_count(self) -> int:
        return self._terminal_count

    @property
    def prefix_count(self) -> int:
        return self._prefix_count

    def terminal_increment(self) -> int:
        self._terminal_count += 1
        return self.terminal_count

    def prefix_increment(self) -> int:
        self._prefix_count += 1
        return self.prefix_count

class Trie_Tree(Generic[T]):
    def __init__(self):
        """ Trie 木を生成する.
        """

        self._root = Trie_Node(None)
        self._size = 1

    @property
    def root(self) -> Trie_Node[T]:
        return self._root

    def insert(self, S: Iterable[T], start_node: Trie_Node[T] = None):
        """ Trie 木に列 S を登録する.

        Args:
            S (Iterable[T]): Trie 木に登録する.
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.
        """

        node = start_node if start_node is not None else self.root

        node.prefix_increment()
        for x in S:
            if x not in node.next:
                node.next[x] = Trie_Node(x)
                self._size += 1

            node = node.next[x]
            node.prefix_increment()

        node.terminal_increment()

    def count(self, S: Iterable[T], start_node: Trie_Node[T] = None) -> int:
        """ Trie 木に登録している S の数を求める.

        Args:
            S (Iterable[T]): 探索対象の列
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.

        Returns:
            int: Trie 木に登録している S の数
        """

        node = start_node if start_node is not None else self.root
        for x in S:
            if x not in node.next:
                return 0

            node = node.next[x]

        return node.terminal_count

    def search(self, S: Iterable[T], start_node: Trie_Node[T] = None) -> bool:
        """ Trie 木に列 S は登録されているか?

        Args:
            S (Iterable[T]): 探索対象の列
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.

        Returns:
            bool: Trie 木に列 S は登録されているか?
        """
        return self.count(S, start_node) > 0

    def __contains__(self, S: Iterable[T]) -> bool:
        """ 列 S が存在するかどうかを判定する.

        S: 列
        """
        return self.search(S)

    def search_prefixing(self, S: Iterable[T], start_node: Trie_Node[T] = None, equal: bool = True) -> bool:
        """ Trie 木に登録されている列 S が prefix となるような列は登録されているか?

        Args:
            S (Iterable[T]): 探索対象の列
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.
            equal (bool, optional): False にすると, 条件が "真の prefix" になる. Defaults to True.

        Returns:
            bool: Trie 木に列 S が prefix となるような列は登録されているか?
        """

        return self.count_prefixing(S, start_node, equal)

    def count_prefixing(self, S: Iterable[T], start_node: Trie_Node[T] = None, equal: bool = True) -> int:
        """ Trie 木に登録されている列 S が prefix となるような列の数を求める

        Args:
            S (Iterable[T]): 探索対象の列
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.

        Returns:
            int: Trie 木に列 S が prefix となるような列の数
        """

        node = start_node if start_node is not None else self.root
        for x in S:
            if x not in node.next:
                return False
            node = node.next[x]

        if equal:
            return node.prefix_count
        else:
            return node.prefix_count - node.terminal_count

    def search_prefixed(self, S: Iterable[T], start_node: Trie_Node[T] = None, equal = True):
        """ Trie 木に登録されている列 S を prefix となるような列は存在するか?

        Args:
            S (Iterable[T]): 探索対象の列
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.
            equal (bool, optional): False にすると, 条件が "真の prefix" になる. Defaults to True.

        Returns:
            bool: Trie 木に登録されている列 S を prefix となるような列は存在するか?
        """

        return self.search_prefixed(S, start_node, equal)

    def count_prefixed(self, S: Iterable[T], start_node: Trie_Node[T] = None, equal: bool = True) -> int:
        """ Trie 木に登録されている列 S を prefix となるような列の数を求める

        Args:
            S (Iterable[T]): 探索対象の列
            start_node (Trie_Node[T], optional): 探索を開始する Trie_Node. None のときは根から. Defaults to None.
            equal (bool, optional): False にすると, 条件が "真の prefix" になる. Defaults to True.

        Returns:
            bool: Trie 木に登録されている列 S を prefix となるような列の数
        """

        node = start_node if start_node is not None else self.root
        count = node.terminal_count
        for x in S:
            if x not in node.next:
                return count

            node = node.next[x]
            count += node.terminal_count

        if equal:
            return count
        else:
            return count - node.terminal_count

    def count_all(self) -> int:
        """ Trie 木に登録されている列の数を求める.

        Returns:
            int: Trie 木に登録されている列の数
        """

        return self.root.prefix_count

    @property
    def size(self) -> int:
        """ Trie 木を構成しているノードの数を求める.

        Returns:
            int: Trie 木を構成しているノードの数
        """
        return self._size

    def search_trail(self, S: Iterable[T]) -> list[Trie_Node[T]]:
        """ S を探索する際に見た Trie_Node のリストを求める.

        Args:
            S (Iterable[T]): 列

        Returns:
            list[Trie_Node[T]]: S を探索する際に見た Trie_Node のリスト (存在しないことが確定すると打ち切られる).
        """

        trail = [self.root]
        current = self.root
        for x in S:
            if x not in current.next:
                break

            current = current.next[x]
            trail.append(current)

        return trail

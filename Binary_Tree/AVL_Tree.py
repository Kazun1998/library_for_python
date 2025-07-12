# Reference:
# https://yottagin.com/?p=4157

from typing import TypeVar, Generic

OrderedKey = TypeVar("OrderedKey")
AVLValue = TypeVar("AVLValue")
class AVL_Node(Generic[OrderedKey, AVLValue]):
    def __init__(self, key: OrderedKey, value: AVLValue):
        self.__key = key
        self.value = value
        self.left: AVL_Node[OrderedKey, AVLValue] = None
        self.right: AVL_Node[OrderedKey, AVLValue] = None
        self.height = 1
        self.size = 1

    @property
    def key(self) -> OrderedKey:
        return self.__key

    def __str__(self) -> str:
        return f"key: {self.key}, value: {self.value}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(key={self.key}, value={self.value})"

class Adelson_Velsky_and_Landis_Tree(Generic[OrderedKey, AVLValue]):
    def __init__(self):
        self.root: AVL_Node[OrderedKey, AVLValue] = None
        self.__length=0

    def __len__(self) -> int:
        return self.__length

    def insert(self, key: OrderedKey, value: AVLValue = None):
        """ キー key の値を value に upsert する.

        Args:
            key (OrderedKey): キー
            value (AVLValue, optional): 値. Defaults to None.
        """

        self.root=self.__insert(self.root, key, value)

    def __insert(self, root: AVL_Node[OrderedKey, AVLValue], key: OrderedKey, value: AVLValue) -> AVL_Node[OrderedKey, AVLValue]:
        if not root:
            self.__length+=1
            return AVL_Node(key, value)
        elif key==root.key:
            root.value=value
            return root
        elif key<root.key:
            root.left=self.__insert(root.left, key, value)
        else:
            root.right=self.__insert(root.right, key, value)

        root.height=1+max(self.get_height(root.left), self.get_height(root.right))
        root.size=1+self.get_size(root.left)+self.get_size(root.right)

        bias=self.get_bias(root)

        # Case I : Left Left
        if bias>1 and key<root.left.key:
            return self.right_rotation(root)

        # Case II : Right Right
        if bias<-1 and key>root.right.key:
            return self.left_rotation(root)

        # Case III : Left Right
        if bias>1 and key>root.left.key:
            root.left=self.left_rotation(root.left)
            return self.right_rotation(root)

        # Case IV : Right Left
        if bias<-1 and key<root.right.key:
            root.right=self.right_rotation(root.right)
            return self.left_rotation(root)

        return root

    def delete(self, key: OrderedKey):
        """ キー key に保存されていた情報を削除する (元から存在しない場合は不変になる).

        Args:
            key (OrderedKey): 削除するキー
        """

        self.root=self.__delete(self.root, key)

    def __delete(self, root: AVL_Node[OrderedKey, AVLValue], key: OrderedKey, mode=1) -> AVL_Node[OrderedKey, AVLValue]:
        if not root:
            return root
        elif key<root.key:
            root.left=self.__delete(root.left, key, mode)
        elif key>root.key:
            root.right=self.__delete(root.right, key, mode)
        else:
            self.__length-=mode
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp

            temp=root.right
            while temp.left:
                temp=temp.left
            root.key=temp.key
            root.value=temp.value
            root.right=self.__delete(root.right, temp.key, mode=0)

        if root is None:
            return root

        root.height=1+max(self.get_height(root.left), self.get_height(root.right))
        root.size=1+self.get_size(root.left)+self.get_size(root.right)

        bias=self.get_bias(root)

        # Case I : Left Left
        if bias>1 and self.get_bias(root.left)>=0:
            return self.right_rotation(root)

        # Case II : Right Right
        if bias<-1 and self.get_bias(root.right)<=0:
            return self.left_rotation(root)

        # Case III : Left Right
        if bias>1 and self.get_bias(root.left)<0:
            root.left=self.left_rotation(root.left)
            return self.right_rotation(root)

        # Case IV : Right Left
        if bias<-1 and self.get_bias(root.right)>0:
            root.right=self.right_rotation(root.right)
            return self.left_rotation(root)
        return root

    def left_rotation(self, x: AVL_Node[OrderedKey, AVLValue]) -> AVL_Node[OrderedKey, AVLValue]:
        y=x.right
        z=y.left

        y.left=x
        x.right=z

        x.height=1+max(self.get_height(x.left), self.get_height(x.right))
        y.height=1+max(self.get_height(y.left), self.get_height(y.right))

        x.size=1+self.get_size(x.left)+self.get_size(x.right)
        y.size=1+self.get_size(y.left)+self.get_size(y.right)

        return y

    def right_rotation(self, x: AVL_Node[OrderedKey, AVLValue]) -> AVL_Node[OrderedKey, AVLValue]:
        y=x.left
        z=y.right

        y.right=x
        x.left=z

        x.height=1+max(self.get_height(x.left), self.get_height(x.right))
        y.height=1+max(self.get_height(y.left), self.get_height(y.right))

        x.size=1+self.get_size(x.left)+self.get_size(x.right)
        y.size=1+self.get_size(y.left)+self.get_size(y.right)

        return y

    def get_height(self, root: AVL_Node[OrderedKey, AVLValue]) -> int:
        if not root:
            return 0
        return root.height

    def get_bias(self, root: AVL_Node[OrderedKey, AVLValue]) -> int:
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)

    def get_size(self, node: AVL_Node[OrderedKey, AVLValue]) -> int:
        if not node:
            return 0
        else:
            return node.size

    def next(self, key: OrderedKey, equal=True, default=None) -> OrderedKey:
        """ この AVL 木に保存されている key 以上であるキーのうち, 最小のキーを求める.

        Args:
            key (OrderedKey): 探索するキー
            equal (bool, optional): False にすると, "以上" が "より大きい" になる. Defaults to True.
            default (optional): key 以下のキーが存在しない場合の返り値. Defaults to None.

        Returns:
            OrderedKey: key 以上の最小のキー
        """

        if self.root is None:
            return default

        flag=0
        x=default
        node=self.root
        while node:
            if key==node.key and equal:
                return key
            if key<node.key:
                if flag:
                    x=min(x, node.key)
                else:
                    x=node.key
                    flag=1
                node=node.left
            else:
                node=node.right
        return x

    def previous(self, key: OrderedKey, equal: bool =True, default = None) -> OrderedKey:
        """ この AVL 木に保存されている key 以下であるキーのうち, 最大のキーを求める.

        Args:
            key (OrderedKey): 探索するキー
            equal (bool, optional): False にすると, "以下" が "未満" になる. Defaults to True.
            default (optional): key 以下のキーが存在しない場合の返り値. Defaults to None.

        Returns:
            OrderedKey: key 以下の最大のキー
        """

        if self.root is None:
            return default

        flag=0
        x=default
        node=self.root
        while node:
            if key==node.key and equal:
                return key
            if node.key<key:
                if flag:
                    x=max(x, node.key)
                else:
                    x=node.key
                    flag=1
                node=node.right
            else:
                node=node.left
        return x

    def kth_element(self, k: OrderedKey) -> OrderedKey:
        """ k (0-indexed) 番目に小さいキー (k<0 のときは abs(-k)-1 番目に大きいキー (リストのインデックスと同様))

        Args:
            k (OrderedKey): キーの順番

        Returns:
            OrderedKey: k 番目に小さいキー
        """

        if k<0:
            k+=len(self)

        assert 0<=k<len(self)

        node=self.root
        while True:
            t=self.get_size(node.left)
            if t==k:
                return node.key
            elif k<t:
                node=node.left
            else:
                k-=t+1
                node=node.right

    def __setitem__(self, key: OrderedKey, value: AVLValue):
        self.insert(key, value)

    def __getitem__(self, key: OrderedKey) -> AVLValue:
        node=self.root
        while node:
            if key==node.key:
                return node.value
            if key<node.key:
                node=node.left
            else:
                node=node.right
        raise KeyError(key)

    def get(self, key: OrderedKey, default=None) -> AVLValue:
        """ キー key に保存されている値を求める (存在しない場合は default).

        Args:
            key (OrderedKey): 探索するキー
            default (optional): キー key が存在しない場合の返り値. Defaults to None.

        Returns:
            AVLValue: キー key に保存されてい値
        """

        node=self.root
        while node:
            if key==node.key:
                return node.value
            if key<node.key:
                node=node.left
            else:
                node=node.right
        return default

    def __contains__(self, key: OrderedKey) -> bool:
        node=self.root
        while node:
            if key==node.key:
                return True
            if key<node.key:
                node=node.left
            else:
                node=node.right
        return False

    def get_min(self, default=None) -> OrderedKey:
        """ キーの最小値を取得する.

        Args:
            default (optional): 木が空であるときの返り値. Defaults to None.

        Returns:
            OrderedKey: 最小のキー
        """

        if self.root is None:
            return default

        node=self.root
        while node.left:
            node=node.left
        return node.key

    def get_max(self, default=None) -> OrderedKey:
        """ キーの最大値を取得する.

        Args:
            default (optional): 木が空であるときの返り値. Defaults to None.

        Returns:
            OrderedKey: 最大のキー
        """

        if self.root is None:
            return default

        node=self.root
        while node.right:
            node=node.right
        return node.key

    def pop_min(self) -> OrderedKey:
        """ キーの最小値を出力し, その最小のキーが持っていた情報を削除する..

        Returns:
            OrderedKey: 最小のキー
        """

        key=self.get_min()
        if key is not None:
            self.delete(key)
        return key

    def pop_max(self) -> OrderedKey:
        """ キーの最大値を出力し, その最大のキーが持っていた情報を削除する..

        Returns:
            OrderedKey: 最大のキー
        """

        key=self.get_max()
        if key is not None:
            self.delete(key)
        return key

    def keys(self):
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            X.append(node.key)
            dfs(node.right)

        X=[]
        dfs(self.root)
        return X

# Reference:
# https://yottagin.com/?p=4157

class AVL_Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.height=1
        self.size=1

    def __str__(self):
        return "key: {}, value: {}".format(self.key, self.value)

    def __repr__(self):
        return "[AVL Node]: "+str(self)

class Adelson_Velsky_and_Landis_Tree:
    def __init__(self):
        self.root=None
        self.__length=0

    def __len__(self):
        return self.__length

    def insert(self, key, value=None):
        self.root=self.__insert(self.root, key, value)

    def __insert(self, root, key, value):
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

    def delete(self, key):
        self.root=self.__delete(self.root, key)

    def __delete(self, root, key, mode=1):
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

    def left_rotation(self, x):
        y=x.right
        z=y.left

        y.left=x
        x.right=z

        x.height=1+max(self.get_height(x.left), self.get_height(x.right))
        y.height=1+max(self.get_height(y.left), self.get_height(y.right))

        x.size=1+self.get_size(x.left)+self.get_size(x.right)
        y.size=1+self.get_size(y.left)+self.get_size(y.right)

        return y

    def right_rotation(self, x):
        y=x.left
        z=y.right

        y.right=x
        x.left=z

        x.height=1+max(self.get_height(x.left), self.get_height(x.right))
        y.height=1+max(self.get_height(y.left), self.get_height(y.right))

        x.size=1+self.get_size(x.left)+self.get_size(x.right)
        y.size=1+self.get_size(y.left)+self.get_size(y.right)

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_bias(self, root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)

    def get_size(self, node):
        if not node:
            return 0
        else:
            return node.size

    def next(self, key, equal=True, default=None):
        """ key 以上で最小のキーを探す. """

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

    def previous(self, key, equal=True, default=None):
        """ key 以下で最大のキーを探す. """

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

    def kth_element(self, k):
        """ k (0-indexed) 番目に小さいキー (k<0 のときは (-k)-1 番目に大きいキー (リストのインデックスと同様))"""

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

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        node=self.root
        while node:
            if key==node.key:
                return node.value
            if key<node.key:
                node=node.left
            else:
                node=node.right
        raise KeyError(key)

    def get(self, key, default=None):
        node=self.root
        while node:
            if key==node.key:
                return node.value
            if key<node.key:
                node=node.left
            else:
                node=node.right
        return default

    def __contains__(self, key):
        node=self.root
        while node:
            if key==node.key:
                return True
            if key<node.key:
                node=node.left
            else:
                node=node.right
        return False

    def get_min(self, default=None):
        if self.root is None:
            return default

        node=self.root
        while node.left:
            node=node.left
        return node.key

    def get_max(self, default=None):
        if self.root is None:
            return default

        node=self.root
        while node.right:
            node=node.right
        return node.key

    def pop_min(self):
        key=self.get_min()
        if key is not None:
            self.delete(key)
        return key

    def pop_max(self):
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

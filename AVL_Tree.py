""" Referecnces
https://yottagin.com/?p=4157

[insert]
10^5 queries: 500 [ms]
2 x 10^5 queries: 1000 [ms]
3 x 10^5 queries: 1200 [ms]
4 x 10^5 queries: 1600 [ms]
5 x 10^5 queries: 2000 [ms]
"""

class Adelson_Velsky_and_Landis_Tree:
    class  AVL_Node:
        def __init__(self, key, value):
            self.key=key
            self.value=value
            self.parent=None
            self.left=None
            self.right=None
            self.height=1

        def __str__(self):
            return "key: {}, value: {}".format(self.key ,self.value)

        def __repr__(self):
            return "[AVL Node] "+str(self)

        def get_bias(self):
            if self is None:
                return 0

            left=self.left.height if self.left is not None else 0
            right=self.right.height if self.right is not None else 0
            return left-right

        def set_height(self):
            left=self.left.height if self.left is not None else 0
            right=self.right.height if self.right is not None else 0
            self.height=1+max(left, right)
            return

        def set_root(self, T):
            """ 根を self に設定する (T には AVL Tree を設定) """

            T.root=self
            if self is not None:
                self.parent=None

        def set_left(self, node):
            """ self の左の子に node を設定する. """

            self.left=node
            if node is not None:
                node.parent=self

        def set_right(self, node):
            """ self の右の子に node を設定する. """

            self.right=node
            if node is not None:
                node.parent=self

    def __init__(self):
        self.root=None
        self.__length=0

    def __len__(self):
        return self.__length

    def left_rotation(self, v):
        p=v.parent
        a=v.right
        b=a.left

        if p is not None:
            if p.key<v.key:
                p.set_right(a)
            else:
                p.set_left(a)
        else:
            self.root=a
            a.parent=None

        a.set_left(v)
        v.set_right(b)

        if b is not None:
            b.set_height()

        v.set_height()
        a.set_height()

    def right_rotation(self, v):
        p=v.parent
        a=v.left
        b=a.right

        if p is not None:
            if p.key<v.key:
                p.set_right(a)
            else:
                p.set_left(a)
        else:
            self.root=a
            a.parent=None

        a.set_right(v)
        v.set_left(b)

        if b is not None:
            b.set_height()

        v.set_height()
        a.set_height()

    def insert(self, key, value=None):
        if not self.root:
            self.root=self.AVL_Node(key, value)
            self.__length+=1
            return

        history=[]
        node=self.root
        while node:
            history.append(node)
            if key==node.key:
                node.value=value
                return
            elif key<node.key:
                node=node.left
            else:
                node=node.right

        self.__length+=1
        new_node=self.AVL_Node(key, value)
        new_node.parent=history[-1]
        if key<history[-1].key:
            history[-1].left=new_node
        else:
            history[-1].right=new_node

        for node in history[::-1]:
            node.set_height()
            bias=node.get_bias()

            flag=0
            if bias>1:
                if key<node.left.key:
                    # Case I : Left Left -> Right Rotation
                    self.right_rotation(node)
                else:
                    # Case II : Left Right -> Left Right Rotation
                    self.left_rotation(node.left)
                    self.right_rotation(node)
                flag=1
            if bias<-1:
                if node.right.key<key:
                    # Case III : Right Right -> Left Rotation
                    self.left_rotation(node)
                else:
                    # Case IV : Right Left -> Right Left Rotation
                    self.right_rotation(node.right)
                    self.left_rotation(node)
                flag=1

            if flag:
                break
        return

    def discard(self, key):
        history=[]
        node=self.root
        while node:
            history.append(node)
            if key==node.key:
                break
            elif key<node.key:
                node=node.left
            else:
                node=node.right

        if node is None:
            return

        par=node.parent
        if (node.left is None) and (node.right is None):
            if par is not None:
                if key<par.key:
                    par.set_left(None)
                else:
                    par.set_right(None)
            else:
                self.root=None
            history.pop()
        elif node.right is None:
            if par is not None:
                if key<par.key:
                    par.set_left(node.left)
                else:
                    par.set_right(node.left)
            else:
                node.left.set_root(self)
            history.pop()
        elif node.left is None:
            if par is not None:
                if key<par.key:
                    par.set_left(node.right)
                else:
                    par.set_right(node.right)
            else:
                node.right.set_root(self)
            history.pop()
        else:
            count=0
            temp=node.right
            while temp:
                history.append(temp)
                temp=temp.left
                count+=1

            temp=history[-1]
            if count>1:
                node.key=temp.key
                node.value=temp.value

                temp.parent.set_left(temp.right)
                history.pop()
            else:
                # temp=node.right
                if par is not None:
                    if key<par.key:
                        par.set_left(temp)
                    else:
                        par.set_right(temp)
                else:
                    temp.set_root(self)
                temp.set_left(node.left)

        if not history:
            return

        node=history[-1]
        while node:
            node.set_height()
            bias=node.get_bias()

            flag=0
            if bias>1:
                if node.left.get_bias()>=0:
                    # Case I : Left Left -> Right Rotation
                    self.right_rotation(node)
                else:
                    # Case II : Left Right -> Left Right Rotation
                    self.left_rotation(node.left)
                    self.right_rotation(node)
                flag=1
            if bias<-1:
                if node.right.get_bias()<=0:
                    # Case III : Right Right -> Left Rotation
                    self.left_rotation(node)
                else:
                    # Case IV : Right Left -> Right Left Rotation
                    self.right_rotation(node.right)
                    self.left_rotation(node)
                flag=1

            if flag:
                break
            node=node.parent
        return

    def get_min(self):
        node=self.root
        while node.left:
            node=node.left
        return node.key

    def get_max(self):
        node=self.root
        while node.right:
            node=node.right
        return node.key

    def __yield__(self):
        if self.root is None:
            return

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
                    x=min(x,node.key)
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
                    x=max(x,node.key)
                else:
                    x=node.key
                    flag=1
                node=node.right
            else:
                node=node.left
        return x

    def __contains__(self, key):
        node=self.root

        while node:
            if node.key==key:
                return True
            elif key<node.key:
                node=node.left
            else:
                node=node.right
        return False

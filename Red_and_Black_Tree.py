"""
Reference
http://fujimura2.fiw-web.net/java/mutter/tree/red-black-tree.html
"""

class Red_and_Black_Node:
    def __init__(self, key, value,color=1):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.__color=color # 0 ならば黒, 1 ならば赤
        self.size=1

    def get_color(self):
        return self.__color

    def set_black(self):
        self.__color=0

    def set_red(self):
        self.__color=1

    def is_black(self):
        return self.__color==0

    def is_red(self):
        return self.__color==1

    def __str__(self):
        return "key: {}, value: {}, color: {}".format(self.key, self.value, "Red" if self.__color else "Black")

    def __repr__(self):
        return "[Red and Black Node]: "+str(self)

class Red_and_Black_Tree:
    def __init__(self):
        self.root=None

    def __len__(self):
        return self.get_size(self.root)

    def insert(self, key, value=None):
        if not self.root:
            # Case 0 : new node is root
            self.root=Red_and_Black_Node(key, value, 0)
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

        P=history[-1]
        N=Red_and_Black_Node(key, value)

        if N.key<P.key:
            P.left=N
        else:
            P.right=N

        active=True

        while True:
            if not active:
                self.set_size(N)
                if not history:
                    return

                N=history.pop()
                continue

            # Case 0 : N is root
            if self.is_root(N):
                N.set_black()
                self.set_size(N)
                return

            P=history[-1]
            # Case I
            if self.is_black(P):
                active=False
                self.set_size(N)
                history.pop()
                N=P
                continue

            # N,P is red. Then, exists G (parent of P) and G is red.
            G=history[-2]
            if P.key<G.key:
                U=G.right
            else:
                U=G.left

            # Case II
            if self.is_red(U):
                G.set_red()
                P.set_black()
                U.set_black()
                history.pop(); history.pop()
                self.set_size(N); self.set_size(P)
                N=G
                continue

            # Case III-LR
            if P.key<N.key<G.key:
                self.left_rotation(P,G)
                history.pop()
                history.append(N)
                N,P=P,N

            # Case III-RL
            if G.key<N.key<P.key:
                self.right_rotation(P,G)
                history.pop()
                history.append(N)
                N,P=P,N

            # Case IV-LL:
            if N.key<P.key<G.key:
                if len(history)>=3:
                    Z=history[-3]
                else:
                    Z=None
                self.right_rotation(G,Z)
                P.set_black()
                G.set_red()

                active=False
                self.set_size(N)
                N=history.pop()
                continue

            # Case IV-RR:
            if G.key<P.key<N.key:
                if len(history)>=3:
                    Z=history[-3]
                else:
                    Z=None
                self.left_rotation(G,Z)
                P.set_black()
                G.set_red()

                active=False
                self.set_size(N)
                N=history.pop()
                continue

    def delete(self, key):
        node=self.root

        history=[]
        while node:
            history.append(node)
            if node.key==key:
                break
            elif key<node.key:
                node=node.left
            else:
                node=node.right
        else:
            return

        history.pop()

        K=node
        if K.right:
            history.append(K)
            T=K.right
            while T.left:
                history.append(T)
                T=T.left
            K.key=T.key
            K.value=T.value
        else:
            T=K

        P=history[-1] if history else None

        if (P is None) and (T.left is None) and (T.right is None):
            self.root=None
            return

        if T.left is None:
            N=T.right
        else:
            N=T.left

        if (P is None) or (T.key<P.key):
            direction=0
        else:
            direction=1

        self.child_set(N,P,T.key)

        if self.is_red(T):
            for X in history[::-1]:
                self.set_size(X)
            return

        if self.is_red(N):
            N.set_black()
            for X in history[::-1]:
                self.set_size(X)
            return

        active=True
        while True:
            if not active:
                self.set_size(N)

                if not history:
                    return

                N=history.pop()
                continue

            # Case I : N is root.
            if self.is_root(N):
                self.set_size(N)
                return

            P=history[-1]
            if N:
                # (初回以外は必ずこっちの分岐になる)
                if N.key<P.key:
                    direction=0
                    S=P.right
                else:
                    direction=1
                    S=P.left
            else:
                if direction==1:
                    S=P.left
                else:
                    S=P.right

            L=S.left; R=S.right

            if len(history)>=2:
                G=history[-2]
            else:
                G=None

            # Case II : S is red.
            if self.is_red(S):
                P.set_red(); S.set_black()
                history.pop()
                history.append(S); history.append(P)

                if direction==0:
                    self.left_rotation(P,G)
                    S=L
                else:
                    self.right_rotation(P,G)
                    S=R
                G=history[-2] if len(history)>=2 else None
                L=S.left; R=S.right

            # Case III :
            if self.is_black(P) and self.is_black(L) and self.is_black(R):
                S.set_red()

                self.set_size(N)
                N=history.pop()
                continue

            # Case IV :
            if self.is_red(P) and self.is_black(L) and self.is_black(R):
                P.set_black()
                S.set_red()

                active=False
                self.set_size(N)
                N=history.pop()
                continue

            # Case V
            if self.is_red(L) and self.is_black(R) and direction==0:
                self.right_rotation(S,P)
                self.set_size(S); self.set_size(L)
                S.set_red(); L.set_black()
                S=L

            if self.is_black(L) and self.is_red(R) and direction==1:
                self.left_rotation(S,P)
                self.set_size(S); self.set_size(R)
                S.set_red(); R.set_black()
                S=R

            L=S.left; R=S.right

            # Case VI :
            if self.is_red(R) and direction==0:
                self.left_rotation(P,G)
                self.swap_color(P,S)
                R.set_black()
                history.pop()
                history.append(S); history.append(P)

                active=False
                self.set_size(N)
                N=history.pop()
                continue

            if self.is_red(L) and direction==1:
                self.right_rotation(P,G)
                self.swap_color(P,S)
                L.set_black()
                history.pop()
                history.append(S); history.append(P)

                active=False
                self.set_size(N)
                N=history.pop()
                continue

    def child_set(self, X, Y, key):
        """ Y の子に X を設定する (Y が None ならば, X を根にする) """

        if Y is None:
            self.root=X
        else:
            if key<Y.key:
                Y.left=X
            else:
                Y.right=X
        return

    def right_rotation(self, node, parent):
        X=node.left
        Y=X.right

        if parent is None:
            self.root=X
        else:
            if X.key<parent.key:
                parent.left=X
            else:
                parent.right=X

        X.right=node
        node.left=Y

        self.set_size(node)
        self.set_size(X)

    def left_rotation(self, node, parent):
        X=node.right
        Y=X.left

        if parent is None:
            self.root=X
        else:
            if X.key<parent.key:
                parent.left=X
            else:
                parent.right=X

        X.left=node
        node.right=Y

        self.set_size(node)
        self.set_size(X)

    def get_size(self, X):
        return X.size if X else 0

    def set_size(self, X):
        if X:
            X.size=1+self.get_size(X.left)+self.get_size(X.right)

    def is_black(self, node):
        return (not node) or node.is_black()

    def is_red(self, node):
        return node and node.is_red()

    def is_root(self, node):
        if self.root:
            return node and node.key==self.root.key
        else:
            return node is None

    def swap_color(self, X, Y):
        cx=0 if X.is_black() else 1
        cy=0 if Y.is_black() else 1

        if cy==0:
            X.set_black()
        else:
            X.set_red()

        if cx==0:
            Y.set_black()
        else:
            Y.set_red()

    def get_left(self, X):
        return X.left if X else None

    def get_right(self, X):
        return X.right if X else None

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

        N=self.root
        while True:
            t=self.get_size(N.left)
            if t==k:
                return N.key
            elif k<t:
                N=N.left
            else:
                k-=t+1
                N=N.right

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

        N=self.root
        while N.left:
            N=N.left
        return N.key

    def get_max(self, default=None):
        if self.root is None:
            return default

        N=self.root
        while N.right:
            N=N.right
        return N.key

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

def debug(T):
    def print_node(node, n=0):
        if not node:
            return

        print_node(node.right, n+1)
        print(" "*(4*n), node.key, "(","R" if node.is_red() else "B", ":",node.size,")")
        print_node(node.left, n+1)

    print_node(T.root)
    print("*"*40)

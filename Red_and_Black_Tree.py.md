---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Red_and_Black_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Red_and_Black_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - http://fujimura2.fiw-web.net/java/mutter/tree/red-black-tree.html
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "\"\"\"\nReference\nhttp://fujimura2.fiw-web.net/java/mutter/tree/red-black-tree.html\n\
    \"\"\"\n\nclass Red_and_Black_Node:\n    def __init__(self, key, value,color=1):\n\
    \        self.key=key\n        self.value=value\n        self.left=None\n    \
    \    self.right=None\n        self.__color=color # 0 \u306A\u3089\u3070\u9ED2\
    , 1 \u306A\u3089\u3070\u8D64\n        self.size=1\n\n    def get_color(self):\n\
    \        return self.__color\n\n    def set_black(self):\n        self.__color=0\n\
    \n    def set_red(self):\n        self.__color=1\n\n    def is_black(self):\n\
    \        return self.__color==0\n\n    def is_red(self):\n        return self.__color==1\n\
    \n    def __str__(self):\n        return \"key: {}, value: {}, color: {}\".format(self.key,\
    \ self.value, \"Red\" if self.__color else \"Black\")\n\n    def __repr__(self):\n\
    \        return \"[Red and Black Node]: \"+str(self)\n\nclass Red_and_Black_Tree:\n\
    \    def __init__(self):\n        self.root=None\n\n    def __len__(self):\n \
    \       return self.get_size(self.root)\n\n    def insert(self, key, value=None):\n\
    \        if not self.root:\n            # Case 0 : new node is root\n        \
    \    self.root=Red_and_Black_Node(key, value, 0)\n            return\n\n     \
    \   history=[]\n        node=self.root\n        while node:\n            history.append(node)\n\
    \            if key==node.key:\n                node.value=value\n           \
    \     return\n            elif key<node.key:\n                node=node.left\n\
    \            else:\n                node=node.right\n\n        P=history[-1]\n\
    \        N=Red_and_Black_Node(key, value)\n\n        if N.key<P.key:\n       \
    \     P.left=N\n        else:\n            P.right=N\n\n        active=True\n\n\
    \        while True:\n            if not active:\n                self.set_size(N)\n\
    \                if not history:\n                    return\n\n             \
    \   N=history.pop()\n                continue\n\n            # Case 0 : N is root\n\
    \            if self.is_root(N):\n                N.set_black()\n            \
    \    self.set_size(N)\n                return\n\n            P=history[-1]\n \
    \           # Case I\n            if self.is_black(P):\n                active=False\n\
    \                self.set_size(N)\n                history.pop()\n           \
    \     N=P\n                continue\n\n            # N,P is red. Then, exists\
    \ G (parent of P) and G is red.\n            G=history[-2]\n            if P.key<G.key:\n\
    \                U=G.right\n            else:\n                U=G.left\n\n  \
    \          # Case II\n            if self.is_red(U):\n                G.set_red()\n\
    \                P.set_black()\n                U.set_black()\n              \
    \  history.pop(); history.pop()\n                self.set_size(N); self.set_size(P)\n\
    \                N=G\n                continue\n\n            # Case III-LR\n\
    \            if P.key<N.key<G.key:\n                self.left_rotation(P,G)\n\
    \                history.pop()\n                history.append(N)\n          \
    \      N,P=P,N\n\n            # Case III-RL\n            if G.key<N.key<P.key:\n\
    \                self.right_rotation(P,G)\n                history.pop()\n   \
    \             history.append(N)\n                N,P=P,N\n\n            # Case\
    \ IV-LL:\n            if N.key<P.key<G.key:\n                if len(history)>=3:\n\
    \                    Z=history[-3]\n                else:\n                  \
    \  Z=None\n                self.right_rotation(G,Z)\n                P.set_black()\n\
    \                G.set_red()\n\n                active=False\n               \
    \ self.set_size(N)\n                N=history.pop()\n                continue\n\
    \n            # Case IV-RR:\n            if G.key<P.key<N.key:\n             \
    \   if len(history)>=3:\n                    Z=history[-3]\n                else:\n\
    \                    Z=None\n                self.left_rotation(G,Z)\n       \
    \         P.set_black()\n                G.set_red()\n\n                active=False\n\
    \                self.set_size(N)\n                N=history.pop()\n         \
    \       continue\n\n    def delete(self, key):\n        node=self.root\n\n   \
    \     history=[]\n        while node:\n            history.append(node)\n    \
    \        if node.key==key:\n                break\n            elif key<node.key:\n\
    \                node=node.left\n            else:\n                node=node.right\n\
    \        else:\n            return\n\n        history.pop()\n\n        K=node\n\
    \        if K.right:\n            history.append(K)\n            T=K.right\n \
    \           while T.left:\n                history.append(T)\n               \
    \ T=T.left\n            K.key=T.key\n            K.value=T.value\n        else:\n\
    \            T=K\n\n        P=history[-1] if history else None\n\n        if (P\
    \ is None) and (T.left is None) and (T.right is None):\n            self.root=None\n\
    \            return\n\n        if T.left is None:\n            N=T.right\n   \
    \     else:\n            N=T.left\n\n        if (P is None) or (T.key<P.key):\n\
    \            direction=0\n        else:\n            direction=1\n\n        self.child_set(N,P,T.key)\n\
    \n        if self.is_red(T):\n            for X in history[::-1]:\n          \
    \      self.set_size(X)\n            return\n\n        if self.is_red(N):\n  \
    \          N.set_black()\n            for X in history[::-1]:\n              \
    \  self.set_size(X)\n            return\n\n        active=True\n        while\
    \ True:\n            if not active:\n                self.set_size(N)\n\n    \
    \            if not history:\n                    return\n\n                N=history.pop()\n\
    \                continue\n\n            # Case I : N is root.\n            if\
    \ self.is_root(N):\n                self.set_size(N)\n                return\n\
    \n            P=history[-1]\n            if N:\n                # (\u521D\u56DE\
    \u4EE5\u5916\u306F\u5FC5\u305A\u3053\u3063\u3061\u306E\u5206\u5C90\u306B\u306A\
    \u308B)\n                if N.key<P.key:\n                    direction=0\n  \
    \                  S=P.right\n                else:\n                    direction=1\n\
    \                    S=P.left\n            else:\n                if direction==1:\n\
    \                    S=P.left\n                else:\n                    S=P.right\n\
    \n            L=S.left; R=S.right\n\n            if len(history)>=2:\n       \
    \         G=history[-2]\n            else:\n                G=None\n\n       \
    \     # Case II : S is red.\n            if self.is_red(S):\n                P.set_red();\
    \ S.set_black()\n                history.pop()\n                history.append(S);\
    \ history.append(P)\n\n                if direction==0:\n                    self.left_rotation(P,G)\n\
    \                    S=L\n                else:\n                    self.right_rotation(P,G)\n\
    \                    S=R\n                G=history[-2] if len(history)>=2 else\
    \ None\n                L=S.left; R=S.right\n\n            # Case III :\n    \
    \        if self.is_black(P) and self.is_black(L) and self.is_black(R):\n    \
    \            S.set_red()\n\n                self.set_size(N)\n               \
    \ N=history.pop()\n                continue\n\n            # Case IV :\n     \
    \       if self.is_red(P) and self.is_black(L) and self.is_black(R):\n       \
    \         P.set_black()\n                S.set_red()\n\n                active=False\n\
    \                self.set_size(N)\n                N=history.pop()\n         \
    \       continue\n\n            # Case V\n            if self.is_red(L) and self.is_black(R)\
    \ and direction==0:\n                self.right_rotation(S,P)\n              \
    \  self.set_size(S); self.set_size(L)\n                S.set_red(); L.set_black()\n\
    \                S=L\n\n            if self.is_black(L) and self.is_red(R) and\
    \ direction==1:\n                self.left_rotation(S,P)\n                self.set_size(S);\
    \ self.set_size(R)\n                S.set_red(); R.set_black()\n             \
    \   S=R\n\n            L=S.left; R=S.right\n\n            # Case VI :\n      \
    \      if self.is_red(R) and direction==0:\n                self.left_rotation(P,G)\n\
    \                self.swap_color(P,S)\n                R.set_black()\n       \
    \         history.pop()\n                history.append(S); history.append(P)\n\
    \n                active=False\n                self.set_size(N)\n           \
    \     N=history.pop()\n                continue\n\n            if self.is_red(L)\
    \ and direction==1:\n                self.right_rotation(P,G)\n              \
    \  self.swap_color(P,S)\n                L.set_black()\n                history.pop()\n\
    \                history.append(S); history.append(P)\n\n                active=False\n\
    \                self.set_size(N)\n                N=history.pop()\n         \
    \       continue\n\n    def child_set(self, X, Y, key):\n        \"\"\" Y \u306E\
    \u5B50\u306B X \u3092\u8A2D\u5B9A\u3059\u308B (Y \u304C None \u306A\u3089\u3070\
    , X \u3092\u6839\u306B\u3059\u308B) \"\"\"\n\n        if Y is None:\n        \
    \    self.root=X\n        else:\n            if key<Y.key:\n                Y.left=X\n\
    \            else:\n                Y.right=X\n        return\n\n    def right_rotation(self,\
    \ node, parent):\n        X=node.left\n        Y=X.right\n\n        if parent\
    \ is None:\n            self.root=X\n        else:\n            if X.key<parent.key:\n\
    \                parent.left=X\n            else:\n                parent.right=X\n\
    \n        X.right=node\n        node.left=Y\n\n        self.set_size(node)\n \
    \       self.set_size(X)\n\n    def left_rotation(self, node, parent):\n     \
    \   X=node.right\n        Y=X.left\n\n        if parent is None:\n           \
    \ self.root=X\n        else:\n            if X.key<parent.key:\n             \
    \   parent.left=X\n            else:\n                parent.right=X\n\n     \
    \   X.left=node\n        node.right=Y\n\n        self.set_size(node)\n       \
    \ self.set_size(X)\n\n    def get_size(self, X):\n        return X.size if X else\
    \ 0\n\n    def set_size(self, X):\n        if X:\n            X.size=1+self.get_size(X.left)+self.get_size(X.right)\n\
    \n    def is_black(self, node):\n        return (not node) or node.is_black()\n\
    \n    def is_red(self, node):\n        return node and node.is_red()\n\n    def\
    \ is_root(self, node):\n        if self.root:\n            return node and node.key==self.root.key\n\
    \        else:\n            return node is None\n\n    def swap_color(self, X,\
    \ Y):\n        cx=0 if X.is_black() else 1\n        cy=0 if Y.is_black() else\
    \ 1\n\n        if cy==0:\n            X.set_black()\n        else:\n         \
    \   X.set_red()\n\n        if cx==0:\n            Y.set_black()\n        else:\n\
    \            Y.set_red()\n\n    def get_left(self, X):\n        return X.left\
    \ if X else None\n\n    def get_right(self, X):\n        return X.right if X else\
    \ None\n\n    def next(self, key, equal=True, default=None):\n        \"\"\" key\
    \ \u4EE5\u4E0A\u3067\u6700\u5C0F\u306E\u30AD\u30FC\u3092\u63A2\u3059. \"\"\"\n\
    \n        if self.root is None:\n            return default\n\n        flag=0\n\
    \        x=default\n        node=self.root\n        while node:\n            if\
    \ key==node.key and equal:\n                return key\n            if key<node.key:\n\
    \                if flag:\n                    x=min(x, node.key)\n          \
    \      else:\n                    x=node.key\n                    flag=1\n   \
    \             node=node.left\n            else:\n                node=node.right\n\
    \        return x\n\n    def previous(self, key, equal=True, default=None):\n\
    \        \"\"\" key \u4EE5\u4E0B\u3067\u6700\u5927\u306E\u30AD\u30FC\u3092\u63A2\
    \u3059. \"\"\"\n\n        if self.root is None:\n            return default\n\n\
    \        flag=0\n        x=default\n        node=self.root\n        while node:\n\
    \            if key==node.key and equal:\n                return key\n       \
    \     if node.key<key:\n                if flag:\n                    x=max(x,\
    \ node.key)\n                else:\n                    x=node.key\n         \
    \           flag=1\n                node=node.right\n            else:\n     \
    \           node=node.left\n        return x\n\n    def kth_element(self, k):\n\
    \        \"\"\" k (0-indexed) \u756A\u76EE\u306B\u5C0F\u3055\u3044\u30AD\u30FC\
    \ (k<0 \u306E\u3068\u304D\u306F (-k)-1 \u756A\u76EE\u306B\u5927\u304D\u3044\u30AD\
    \u30FC (\u30EA\u30B9\u30C8\u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u3068\u540C\
    \u69D8))\"\"\"\n\n        if k<0:\n            k+=len(self)\n\n        assert\
    \ 0<=k<len(self)\n\n        N=self.root\n        while True:\n            t=self.get_size(N.left)\n\
    \            if t==k:\n                return N.key\n            elif k<t:\n \
    \               N=N.left\n            else:\n                k-=t+1\n        \
    \        N=N.right\n\n    def __setitem__(self, key, value):\n        self.insert(key,\
    \ value)\n\n    def __getitem__(self, key):\n        node=self.root\n        while\
    \ node:\n            if key==node.key:\n                return node.value\n  \
    \          if key<node.key:\n                node=node.left\n            else:\n\
    \                node=node.right\n        raise KeyError(key)\n\n    def get(self,\
    \ key, default=None):\n        node=self.root\n        while node:\n         \
    \   if key==node.key:\n                return node.value\n            if key<node.key:\n\
    \                node=node.left\n            else:\n                node=node.right\n\
    \        return default\n\n    def __contains__(self, key):\n        node=self.root\n\
    \        while node:\n            if key==node.key:\n                return True\n\
    \            if key<node.key:\n                node=node.left\n            else:\n\
    \                node=node.right\n        return False\n\n    def get_min(self,\
    \ default=None):\n        if self.root is None:\n            return default\n\n\
    \        N=self.root\n        while N.left:\n            N=N.left\n        return\
    \ N.key\n\n    def get_max(self, default=None):\n        if self.root is None:\n\
    \            return default\n\n        N=self.root\n        while N.right:\n \
    \           N=N.right\n        return N.key\n\n    def pop_min(self):\n      \
    \  key=self.get_min()\n        if key is not None:\n            self.delete(key)\n\
    \        return key\n\n    def pop_max(self):\n        key=self.get_max()\n  \
    \      if key is not None:\n            self.delete(key)\n        return key\n"
  dependsOn: []
  isVerificationFile: false
  path: Red_and_Black_Tree.py
  requiredBy: []
  timestamp: '2022-12-13 00:29:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-Red_and_Black_Tree.test.py
documentation_of: Red_and_Black_Tree.py
layout: document
redirect_from:
- /library/Red_and_Black_Tree.py
- /library/Red_and_Black_Tree.py.html
title: Red_and_Black_Tree.py
---

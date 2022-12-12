---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
    title: test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://yottagin.com/?p=4157
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Reference:\n# https://yottagin.com/?p=4157\n\nclass AVL_Node:\n    def\
    \ __init__(self, key, value):\n        self.key=key\n        self.value=value\n\
    \        self.left=None\n        self.right=None\n        self.height=1\n    \
    \    self.size=1\n\n    def __str__(self):\n        return \"key: {}, value: {}\"\
    .format(self.key, self.value)\n\n    def __repr__(self):\n        return \"[AVL\
    \ Node]: \"+str(self)\n\nclass Adelson_Velsky_and_Landis_Tree:\n    def __init__(self):\n\
    \        self.root=None\n        self.__length=0\n\n    def __len__(self):\n \
    \       return self.__length\n\n    def insert(self, key, value=None):\n     \
    \   self.root=self.__insert(self.root, key, value)\n\n    def __insert(self, root,\
    \ key, value):\n        if not root:\n            self.__length+=1\n         \
    \   return AVL_Node(key, value)\n        elif key==root.key:\n            root.value=value\n\
    \            return root\n        elif key<root.key:\n            root.left=self.__insert(root.left,\
    \ key, value)\n        else:\n            root.right=self.__insert(root.right,\
    \ key, value)\n\n        root.height=1+max(self.get_height(root.left), self.get_height(root.right))\n\
    \        root.size=1+self.get_size(root.left)+self.get_size(root.right)\n\n  \
    \      bias=self.get_bias(root)\n\n        # Case I : Left Left\n        if bias>1\
    \ and key<root.left.key:\n            return self.right_rotation(root)\n\n   \
    \     # Case II : Right Right\n        if bias<-1 and key>root.right.key:\n  \
    \          return self.left_rotation(root)\n\n        # Case III : Left Right\n\
    \        if bias>1 and key>root.left.key:\n            root.left=self.left_rotation(root.left)\n\
    \            return self.right_rotation(root)\n\n        # Case IV : Right Left\n\
    \        if bias<-1 and key<root.right.key:\n            root.right=self.right_rotation(root.right)\n\
    \            return self.left_rotation(root)\n\n        return root\n\n    def\
    \ delete(self, key):\n        self.root=self.__delete(self.root, key)\n\n    def\
    \ __delete(self, root, key, mode=1):\n        if not root:\n            return\
    \ root\n        elif key<root.key:\n            root.left=self.__delete(root.left,\
    \ key, mode)\n        elif key>root.key:\n            root.right=self.__delete(root.right,\
    \ key, mode)\n        else:\n            self.__length-=mode\n            if root.left\
    \ is None:\n                temp=root.right\n                root=None\n     \
    \           return temp\n            elif root.right is None:\n              \
    \  temp=root.left\n                root=None\n                return temp\n\n\
    \            temp=root.right\n            while temp.left:\n                temp=temp.left\n\
    \            root.key=temp.key\n            root.value=temp.value\n          \
    \  root.right=self.__delete(root.right, temp.key, mode=0)\n\n        if root is\
    \ None:\n            return root\n\n        root.height=1+max(self.get_height(root.left),\
    \ self.get_height(root.right))\n        root.size=1+self.get_size(root.left)+self.get_size(root.right)\n\
    \n        bias=self.get_bias(root)\n\n        # Case I : Left Left\n        if\
    \ bias>1 and self.get_bias(root.left)>=0:\n            return self.right_rotation(root)\n\
    \n        # Case II : Right Right\n        if bias<-1 and self.get_bias(root.right)<=0:\n\
    \            return self.left_rotation(root)\n\n        # Case III : Left Right\n\
    \        if bias>1 and self.get_bias(root.left)<0:\n            root.left=self.left_rotation(root.left)\n\
    \            return self.right_rotation(root)\n\n        # Case IV : Right Left\n\
    \        if bias<-1 and self.get_bias(root.right)>0:\n            root.right=self.right_rotation(root.right)\n\
    \            return self.left_rotation(root)\n        return root\n\n    def left_rotation(self,\
    \ x):\n        y=x.right\n        z=y.left\n\n        y.left=x\n        x.right=z\n\
    \n        x.height=1+max(self.get_height(x.left), self.get_height(x.right))\n\
    \        y.height=1+max(self.get_height(y.left), self.get_height(y.right))\n\n\
    \        x.size=1+self.get_size(x.left)+self.get_size(x.right)\n        y.size=1+self.get_size(y.left)+self.get_size(y.right)\n\
    \n        return y\n\n    def right_rotation(self, x):\n        y=x.left\n   \
    \     z=y.right\n\n        y.right=x\n        x.left=z\n\n        x.height=1+max(self.get_height(x.left),\
    \ self.get_height(x.right))\n        y.height=1+max(self.get_height(y.left), self.get_height(y.right))\n\
    \n        x.size=1+self.get_size(x.left)+self.get_size(x.right)\n        y.size=1+self.get_size(y.left)+self.get_size(y.right)\n\
    \n        return y\n\n    def get_height(self, root):\n        if not root:\n\
    \            return 0\n        return root.height\n\n    def get_bias(self, root):\n\
    \        if not root:\n            return 0\n        return self.get_height(root.left)-self.get_height(root.right)\n\
    \n    def get_size(self, node):\n        if not node:\n            return 0\n\
    \        else:\n            return node.size\n\n    def next(self, key, equal=True,\
    \ default=None):\n        \"\"\" key \u4EE5\u4E0A\u3067\u6700\u5C0F\u306E\u30AD\
    \u30FC\u3092\u63A2\u3059. \"\"\"\n\n        if self.root is None:\n          \
    \  return default\n\n        flag=0\n        x=default\n        node=self.root\n\
    \        while node:\n            if key==node.key and equal:\n              \
    \  return key\n            if key<node.key:\n                if flag:\n      \
    \              x=min(x, node.key)\n                else:\n                   \
    \ x=node.key\n                    flag=1\n                node=node.left\n   \
    \         else:\n                node=node.right\n        return x\n\n    def\
    \ previous(self, key, equal=True, default=None):\n        \"\"\" key \u4EE5\u4E0B\
    \u3067\u6700\u5927\u306E\u30AD\u30FC\u3092\u63A2\u3059. \"\"\"\n\n        if self.root\
    \ is None:\n            return default\n\n        flag=0\n        x=default\n\
    \        node=self.root\n        while node:\n            if key==node.key and\
    \ equal:\n                return key\n            if node.key<key:\n         \
    \       if flag:\n                    x=max(x, node.key)\n                else:\n\
    \                    x=node.key\n                    flag=1\n                node=node.right\n\
    \            else:\n                node=node.left\n        return x\n\n    def\
    \ kth_element(self, k):\n        \"\"\" k (0-indexed) \u756A\u76EE\u306B\u5C0F\
    \u3055\u3044\u30AD\u30FC (k<0 \u306E\u3068\u304D\u306F (-k)-1 \u756A\u76EE\u306B\
    \u5927\u304D\u3044\u30AD\u30FC (\u30EA\u30B9\u30C8\u306E\u30A4\u30F3\u30C7\u30C3\
    \u30AF\u30B9\u3068\u540C\u69D8))\"\"\"\n\n        if k<0:\n            k+=len(self)\n\
    \n        assert 0<=k<len(self)\n\n        node=self.root\n        while True:\n\
    \            t=self.get_size(node.left)\n            if t==k:\n              \
    \  return node.key\n            elif k<t:\n                node=node.left\n  \
    \          else:\n                k-=t+1\n                node=node.right\n\n\
    \    def __setitem__(self, key, value):\n        self.insert(key, value)\n\n \
    \   def __getitem__(self, key):\n        node=self.root\n        while node:\n\
    \            if key==node.key:\n                return node.value\n          \
    \  if key<node.key:\n                node=node.left\n            else:\n     \
    \           node=node.right\n        raise KeyError(key)\n\n    def get(self,\
    \ key, default=None):\n        node=self.root\n        while node:\n         \
    \   if key==node.key:\n                return node.value\n            if key<node.key:\n\
    \                node=node.left\n            else:\n                node=node.right\n\
    \        return default\n\n    def __contains__(self, key):\n        node=self.root\n\
    \        while node:\n            if key==node.key:\n                return True\n\
    \            if key<node.key:\n                node=node.left\n            else:\n\
    \                node=node.right\n        return False\n\n    def get_min(self,\
    \ default=None):\n        if self.root is None:\n            return default\n\n\
    \        node=self.root\n        while node.left:\n            node=node.left\n\
    \        return node.key\n\n    def get_max(self, default=None):\n        if self.root\
    \ is None:\n            return default\n\n        node=self.root\n        while\
    \ node.right:\n            node=node.right\n        return node.key\n\n    def\
    \ pop_min(self):\n        key=self.get_min()\n        if key is not None:\n  \
    \          self.delete(key)\n        return key\n\n    def pop_max(self):\n  \
    \      key=self.get_max()\n        if key is not None:\n            self.delete(key)\n\
    \        return key\n\n    def keys(self):\n        def dfs(node):\n         \
    \   if node is None:\n                return\n            dfs(node.left)\n   \
    \         X.append(node.key)\n            dfs(node.right)\n\n        X=[]\n  \
    \      dfs(self.root)\n        return X\n\n"
  dependsOn: []
  isVerificationFile: false
  path: AVL_Tree.py
  requiredBy: []
  timestamp: '2022-12-13 00:36:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
documentation_of: AVL_Tree.py
layout: document
redirect_from:
- /library/AVL_Tree.py
- /library/AVL_Tree.py.html
title: AVL_Tree.py
---

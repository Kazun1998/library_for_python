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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.13.5/x64/lib/python3.13/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# Reference:\n# https://yottagin.com/?p=4157\n\nfrom typing import TypeVar,\
    \ Generic\n\nOrderedKey = TypeVar(\"OrderedKey\")\nAVLValue = TypeVar(\"AVLValue\"\
    )\nclass AVL_Node(Generic[OrderedKey, AVLValue]):\n    def __init__(self, key:\
    \ OrderedKey, value: AVLValue):\n        self.__key = key\n        self.value\
    \ = value\n        self.left: AVL_Node[OrderedKey, AVLValue] = None\n        self.right:\
    \ AVL_Node[OrderedKey, AVLValue] = None\n        self.height = 1\n        self.size\
    \ = 1\n\n    @property\n    def key(self) -> OrderedKey:\n        return self.__key\n\
    \n    def __str__(self) -> str:\n        return f\"key: {self.key}, value: {self.value}\"\
    \n\n    def __repr__(self) -> str:\n        return f\"{self.__class__.__name__}(key={self.key},\
    \ value={self.value})\"\n\nclass Adelson_Velsky_and_Landis_Tree(Generic[OrderedKey,\
    \ AVLValue]):\n    def __init__(self):\n        self.root: AVL_Node[OrderedKey,\
    \ AVLValue] = None\n        self.__length = 0\n\n    def __len__(self) -> int:\n\
    \        return self.__length\n\n    def insert(self, key: OrderedKey, value:\
    \ AVLValue = None):\n        \"\"\" \u30AD\u30FC key \u306E\u5024\u3092 value\
    \ \u306B upsert \u3059\u308B.\n\n        Args:\n            key (OrderedKey):\
    \ \u30AD\u30FC\n            value (AVLValue, optional): \u5024. Defaults to None.\n\
    \        \"\"\"\n\n        self.root = self.__insert(self.root, key, value)\n\n\
    \    def __insert(self, root: AVL_Node[OrderedKey, AVLValue], key: OrderedKey,\
    \ value: AVLValue) -> AVL_Node[OrderedKey, AVLValue]:\n        \"\"\" AVL \u6728\
    \u3078\u306E\u30CE\u30FC\u30C9\u306E\u633F\u5165\u3092\u518D\u5E30\u7684\u306B\
    \u884C\u3046.\n\n        Args:\n            root (AVL_Node[OrderedKey, AVLValue]):\
    \ \u90E8\u5206\u6728\u306E\u6839\n            key (OrderedKey): \u30AD\u30FC\n\
    \            value (AVLValue): \u30D0\u30EA\u30E5\u30FC\n\n        Returns:\n\
    \            AVL_Node[OrderedKey, AVLValue]: \u633F\u5165\u5F8C\u306E\u65B0\u305F\
    \u306A\u90E8\u5206\u6728\u306E\u6839\n        \"\"\"\n\n        if not root:\n\
    \            # create\n            self.__length += 1\n            return AVL_Node(key,\
    \ value)\n\n        if key == root.key:\n            # update\n            root.value\
    \ = value\n            return root\n        elif key < root.key:\n           \
    \ # goto left\n            root.left = self.__insert(root.left, key, value)\n\
    \        else:\n            # goto right\n            root.right = self.__insert(root.right,\
    \ key, value)\n\n        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))\n\
    \        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)\n\
    \n        bias = self.get_bias(root)\n\n        # Case I : Left Left\n       \
    \ if bias > 1 and key < root.left.key:\n            return self.right_rotation(root)\n\
    \n        # Case II : Right Right\n        if bias < -1 and key > root.right.key:\n\
    \            return self.left_rotation(root)\n\n        # Case III : Left Right\n\
    \        if bias > 1 and key > root.left.key:\n            root.left = self.left_rotation(root.left)\n\
    \            return self.right_rotation(root)\n\n        # Case IV : Right Left\n\
    \        if bias < -1 and key < root.right.key:\n            root.right = self.right_rotation(root.right)\n\
    \            return self.left_rotation(root)\n\n        return root\n\n    def\
    \ delete(self, key: OrderedKey):\n        \"\"\" \u30AD\u30FC key \u306B\u4FDD\
    \u5B58\u3055\u308C\u3066\u3044\u305F\u60C5\u5831\u3092\u524A\u9664\u3059\u308B\
    \ (\u5143\u304B\u3089\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F\u4E0D\u5909\
    \u306B\u306A\u308B).\n\n        Args:\n            key (OrderedKey): \u524A\u9664\
    \u3059\u308B\u30AD\u30FC\n        \"\"\"\n\n        self.root = self.__delete(self.root,\
    \ key)\n\n    def __delete(self, root: AVL_Node[OrderedKey, AVLValue], key: OrderedKey,\
    \ mode=1) -> AVL_Node[OrderedKey, AVLValue]:\n        \"\"\" AVL \u6728\u3078\u306E\
    \u30CE\u30FC\u30C9\u306E\u524A\u9664\u3092\u518D\u5E30\u7684\u306B\u884C\u3046\
    .\n\n        Args:\n            root (AVL_Node[OrderedKey, AVLValue]): \u90E8\u5206\
    \u6728\u306E\u6839\n            key (OrderedKey): \u30AD\u30FC\n            value\
    \ (AVLValue): \u30D0\u30EA\u30E5\u30FC\n\n        Returns:\n            AVL_Node[OrderedKey,\
    \ AVLValue]: \u524A\u9664\u5F8C\u306E\u65B0\u305F\u306A\u90E8\u5206\u6728\u306E\
    \u6839\n        \"\"\"\n\n        if not root:\n            # empty\n        \
    \    return root\n\n        if key < root.key:\n            # goto left\n    \
    \        root.left = self.__delete(root.left, key, mode)\n        elif key > root.key:\n\
    \            # goto right\n            root.right = self.__delete(root.right,\
    \ key, mode)\n        else:\n            # key == root.key\n            self.__length\
    \ -= mode\n\n            if root.left is None:\n                temp = root.right\n\
    \                root = None\n                return temp\n            elif root.right\
    \ is None:\n                temp = root.left\n                root = None\n  \
    \              return temp\n\n            temp = root.right\n            while\
    \ temp.left:\n                temp = temp.left\n\n            root.key = temp.key\n\
    \            root.value = temp.value\n            root.right = self.__delete(root.right,\
    \ temp.key, mode = 0)\n\n        if root is None:\n            return root\n\n\
    \        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))\n\
    \        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)\n\
    \n        bias = self.get_bias(root)\n\n        # Case I : Left Left\n       \
    \ if bias > 1 and self.get_bias(root.left) >= 0:\n            return self.right_rotation(root)\n\
    \n        # Case II : Right Right\n        if bias < -1 and self.get_bias(root.right)\
    \ <= 0:\n            return self.left_rotation(root)\n\n        # Case III : Left\
    \ Right\n        if bias > 1 and self.get_bias(root.left) < 0:\n            root.left\
    \ = self.left_rotation(root.left)\n            return self.right_rotation(root)\n\
    \n        # Case IV : Right Left\n        if bias < -1 and self.get_bias(root.right)\
    \ > 0:\n            root.right = self.right_rotation(root.right)\n           \
    \ return self.left_rotation(root)\n        return root\n\n    def left_rotation(self,\
    \ x: AVL_Node[OrderedKey, AVLValue]) -> AVL_Node[OrderedKey, AVLValue]:\n    \
    \    \"\"\" x \u3092\u8D77\u70B9\u3068\u3057\u3066, \u5DE6\u56DE\u8EE2\u3092\u884C\
    \u3046 (x \u306E\u53F3\u306E\u5B50\u304C\u65B0\u305F\u306A\u90E8\u5206\u6728\u306E\
    \u6839\u306B\u306A\u308B)\n\n        Args:\n            x (AVL_Node[OrderedKey,\
    \ AVLValue]): \u8D77\u70B9\n\n        Returns:\n            AVL_Node[OrderedKey,\
    \ AVLValue]: \u65B0\u305F\u306A\u90E8\u5206\u6728\u306E\u6839 (\u5143\u306E x\
    \ \u306E\u53F3\u306E\u5B50)\n        \"\"\"\n\n        y = x.right\n        z\
    \ = y.left\n\n        y.left = x\n        x.right = z\n\n        x.height = 1\
    \ + max(self.get_height(x.left), self.get_height(x.right))\n        y.height =\
    \ 1 + max(self.get_height(y.left), self.get_height(y.right))\n\n        x.size\
    \ = 1 + self.get_size(x.left) + self.get_size(x.right)\n        y.size = 1 + self.get_size(y.left)\
    \ + self.get_size(y.right)\n\n        return y\n\n    def right_rotation(self,\
    \ x: AVL_Node[OrderedKey, AVLValue]) -> AVL_Node[OrderedKey, AVLValue]:\n    \
    \    \"\"\" x \u3092\u8D77\u70B9\u3068\u3057\u3066, \u53F3\u56DE\u8EE2\u3092\u884C\
    \u3046 (x \u306E\u5DE6\u306E\u5B50\u304C\u65B0\u305F\u306A\u90E8\u5206\u6728\u306E\
    \u6839\u306B\u306A\u308B)\n\n        Args:\n            x (AVL_Node[OrderedKey,\
    \ AVLValue]): \u8D77\u70B9\n\n        Returns:\n            AVL_Node[OrderedKey,\
    \ AVLValue]: \u65B0\u305F\u306A\u90E8\u5206\u6728\u306E\u6839 (\u5143\u306E x\
    \ \u306E\u5DE6\u306E\u5B50)\n        \"\"\"\n\n        y = x.left\n        z =\
    \ y.right\n\n        y.right = x\n        x.left = z\n\n        x.height = 1 +\
    \ max(self.get_height(x.left), self.get_height(x.right))\n        y.height = 1\
    \ + max(self.get_height(y.left), self.get_height(y.right))\n\n        x.size =\
    \ 1 + self.get_size(x.left) + self.get_size(x.right)\n        y.size = 1 + self.get_size(y.left)\
    \ + self.get_size(y.right)\n\n        return y\n\n    def get_height(self, root:\
    \ AVL_Node[OrderedKey, AVLValue]) -> int:\n        return root.height if root\
    \ else 0\n\n    def get_bias(self, root: AVL_Node[OrderedKey, AVLValue]) -> int:\n\
    \        return self.get_height(root.left) - self.get_height(root.right) if root\
    \ else 0\n\n    def get_size(self, node: AVL_Node[OrderedKey, AVLValue]) -> int:\n\
    \        return node.size if node else 0\n\n    def next(self, key: OrderedKey,\
    \ equal: bool = True, default = None) -> OrderedKey:\n        \"\"\" \u3053\u306E\
    \ AVL \u6728\u306B\u4FDD\u5B58\u3055\u308C\u3066\u3044\u308B key \u4EE5\u4E0A\u3067\
    \u3042\u308B\u30AD\u30FC\u306E\u3046\u3061, \u6700\u5C0F\u306E\u30AD\u30FC\u3092\
    \u6C42\u3081\u308B.\n\n        Args:\n            key (OrderedKey): \u63A2\u7D22\
    \u3059\u308B\u30AD\u30FC\n            equal (bool, optional): False \u306B\u3059\
    \u308B\u3068, \"\u4EE5\u4E0A\" \u304C \"\u3088\u308A\u5927\u304D\u3044\" \u306B\
    \u306A\u308B. Defaults to True.\n            default (optional): key \u4EE5\u4E0B\
    \u306E\u30AD\u30FC\u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\
    \u308A\u5024. Defaults to None.\n\n        Returns:\n            OrderedKey: key\
    \ \u4EE5\u4E0A\u306E\u6700\u5C0F\u306E\u30AD\u30FC\n        \"\"\"\n\n       \
    \ if self.root is None:\n            return default\n\n        flag = 0\n    \
    \    x = default\n        node = self.root\n        while node:\n            if\
    \ key == node.key and equal:\n                return key\n\n            if key\
    \ < node.key:\n                if flag:\n                    x = min(x, node.key)\n\
    \                else:\n                    x = node.key\n                   \
    \ flag = 1\n                node = node.left\n            else:\n            \
    \    node = node.right\n        return x\n\n    def previous(self, key: OrderedKey,\
    \ equal: bool =True, default = None) -> OrderedKey:\n        \"\"\" \u3053\u306E\
    \ AVL \u6728\u306B\u4FDD\u5B58\u3055\u308C\u3066\u3044\u308B key \u4EE5\u4E0B\u3067\
    \u3042\u308B\u30AD\u30FC\u306E\u3046\u3061, \u6700\u5927\u306E\u30AD\u30FC\u3092\
    \u6C42\u3081\u308B.\n\n        Args:\n            key (OrderedKey): \u63A2\u7D22\
    \u3059\u308B\u30AD\u30FC\n            equal (bool, optional): False \u306B\u3059\
    \u308B\u3068, \"\u4EE5\u4E0B\" \u304C \"\u672A\u6E80\" \u306B\u306A\u308B. Defaults\
    \ to True.\n            default (optional): key \u4EE5\u4E0B\u306E\u30AD\u30FC\
    \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306E\u8FD4\u308A\u5024. Defaults\
    \ to None.\n\n        Returns:\n            OrderedKey: key \u4EE5\u4E0B\u306E\
    \u6700\u5927\u306E\u30AD\u30FC\n        \"\"\"\n\n        if self.root is None:\n\
    \            return default\n\n        flag = 0\n        x = default\n       \
    \ node = self.root\n        while node:\n            if key == node.key and equal:\n\
    \                return key\n\n            if node.key < key:\n              \
    \  if flag:\n                    x = max(x, node.key)\n                else:\n\
    \                    x = node.key\n                    flag = 1\n            \
    \    node = node.right\n            else:\n                node = node.left\n\
    \        return x\n\n    def kth_element(self, k: OrderedKey) -> OrderedKey:\n\
    \        \"\"\" k (0-indexed) \u756A\u76EE\u306B\u5C0F\u3055\u3044\u30AD\u30FC\
    \ (k<0 \u306E\u3068\u304D\u306F abs(-k)-1 \u756A\u76EE\u306B\u5927\u304D\u3044\
    \u30AD\u30FC (\u30EA\u30B9\u30C8\u306E\u30A4\u30F3\u30C7\u30C3\u30AF\u30B9\u3068\
    \u540C\u69D8))\n\n        Args:\n            k (OrderedKey): \u30AD\u30FC\u306E\
    \u9806\u756A\n\n        Returns:\n            OrderedKey: k \u756A\u76EE\u306B\
    \u5C0F\u3055\u3044\u30AD\u30FC\n        \"\"\"\n\n        if k < 0:\n        \
    \    k += len(self)\n\n        assert 0 <= k < len(self)\n\n        node=self.root\n\
    \        while True:\n            t = self.get_size(node.left)\n            if\
    \ t == k:\n                return node.key\n            elif k < t:\n        \
    \        node = node.left\n            else:\n                k -= t + 1\n   \
    \             node = node.right\n\n    def __setitem__(self, key: OrderedKey,\
    \ value: AVLValue):\n        self.insert(key, value)\n\n    def __getitem__(self,\
    \ key: OrderedKey) -> AVLValue:\n        node = self.root\n        while node:\n\
    \            if key == node.key:\n                return node.value\n\n      \
    \      if key < node.key:\n                node = node.left\n            else:\n\
    \                node = node.right\n        raise KeyError(key)\n\n    def get(self,\
    \ key: OrderedKey, default=None) -> AVLValue:\n        \"\"\" \u30AD\u30FC key\
    \ \u306B\u4FDD\u5B58\u3055\u308C\u3066\u3044\u308B\u5024\u3092\u6C42\u3081\u308B\
    \ (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\u306F default).\n\n        Args:\n\
    \            key (OrderedKey): \u63A2\u7D22\u3059\u308B\u30AD\u30FC\n        \
    \    default (optional): \u30AD\u30FC key \u304C\u5B58\u5728\u3057\u306A\u3044\
    \u5834\u5408\u306E\u8FD4\u308A\u5024. Defaults to None.\n\n        Returns:\n\
    \            AVLValue: \u30AD\u30FC key \u306B\u4FDD\u5B58\u3055\u308C\u3066\u3044\
    \u5024\n        \"\"\"\n\n        node = self.root\n        while node:\n    \
    \        if key == node.key:\n                return node.value\n\n          \
    \  if key < node.key:\n                node = node.left\n            else:\n \
    \               node = node.right\n        return default\n\n    def __contains__(self,\
    \ key: OrderedKey) -> bool:\n        node = self.root\n        while node:\n \
    \           if key == node.key:\n                return True\n\n            if\
    \ key < node.key:\n                node = node.left\n            else:\n     \
    \           node = node.right\n        return False\n\n    def get_min(self, default=None)\
    \ -> OrderedKey:\n        \"\"\" \u30AD\u30FC\u306E\u6700\u5C0F\u5024\u3092\u53D6\
    \u5F97\u3059\u308B.\n\n        Args:\n            default (optional): \u6728\u304C\
    \u7A7A\u3067\u3042\u308B\u3068\u304D\u306E\u8FD4\u308A\u5024. Defaults to None.\n\
    \n        Returns:\n            OrderedKey: \u6700\u5C0F\u306E\u30AD\u30FC\n \
    \       \"\"\"\n\n        if self.root is None:\n            return default\n\n\
    \        node = self.root\n        while node.left:\n            node = node.left\n\
    \        return node.key\n\n    def get_max(self, default=None) -> OrderedKey:\n\
    \        \"\"\" \u30AD\u30FC\u306E\u6700\u5927\u5024\u3092\u53D6\u5F97\u3059\u308B\
    .\n\n        Args:\n            default (optional): \u6728\u304C\u7A7A\u3067\u3042\
    \u308B\u3068\u304D\u306E\u8FD4\u308A\u5024. Defaults to None.\n\n        Returns:\n\
    \            OrderedKey: \u6700\u5927\u306E\u30AD\u30FC\n        \"\"\"\n\n  \
    \      if self.root is None:\n            return default\n\n        node = self.root\n\
    \        while node.right:\n            node = node.right\n        return node.key\n\
    \n    def pop_min(self) -> OrderedKey:\n        \"\"\" \u30AD\u30FC\u306E\u6700\
    \u5C0F\u5024\u3092\u51FA\u529B\u3057, \u305D\u306E\u6700\u5C0F\u306E\u30AD\u30FC\
    \u304C\u6301\u3063\u3066\u3044\u305F\u60C5\u5831\u3092\u524A\u9664\u3059\u308B\
    ..\n\n        Returns:\n            OrderedKey: \u6700\u5C0F\u306E\u30AD\u30FC\
    \n        \"\"\"\n\n        key = self.get_min()\n        if key is not None:\n\
    \            self.delete(key)\n        return key\n\n    def pop_max(self) ->\
    \ OrderedKey:\n        \"\"\" \u30AD\u30FC\u306E\u6700\u5927\u5024\u3092\u51FA\
    \u529B\u3057, \u305D\u306E\u6700\u5927\u306E\u30AD\u30FC\u304C\u6301\u3063\u3066\
    \u3044\u305F\u60C5\u5831\u3092\u524A\u9664\u3059\u308B..\n\n        Returns:\n\
    \            OrderedKey: \u6700\u5927\u306E\u30AD\u30FC\n        \"\"\"\n\n  \
    \      key = self.get_max()\n        if key is not None:\n            self.delete(key)\n\
    \        return key\n\n    def keys(self) -> list[OrderedKey]:\n        \"\"\"\
    \ \u3053\u306E AVL \u6728\u306B\u4FDD\u5B58\u3055\u308C\u3066\u3044\u308B\u30AD\
    \u30FC\u3092\u6607\u9806\u306B\u51FA\u529B\u3059\u308B.\n\n        Returns:\n\
    \            list[OrderedKey]: \u4FDD\u5B58\u3055\u308C\u3066\u3044\u308B\u30AD\
    \u30FC\n        \"\"\"\n\n        def dfs(node: AVL_Node):\n            if node\
    \ is None:\n                return\n\n            yield from dfs(node.left)\n\
    \            yield node.key\n            yield from dfs(node.right)\n\n      \
    \  return list(dfs(self.root))\n"
  dependsOn: []
  isVerificationFile: false
  path: Binary_Tree/AVL_Tree.py
  requiredBy: []
  timestamp: '2025-07-12 12:38:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test_verify/yosupo_library_checker/Data_Structure/Double_Ended_Priority_Queue-AVL_Tree.test.py
documentation_of: Binary_Tree/AVL_Tree.py
layout: document
redirect_from:
- /library/Binary_Tree/AVL_Tree.py
- /library/Binary_Tree/AVL_Tree.py.html
title: Binary_Tree/AVL_Tree.py
---

---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.0/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Trie_Node():\n    def __init__(self, item):\n        self.item=item\n\
    \        self.next={}\n        self.terminal_count=0\n        self.prefix_count=0\n\
    \n    def __str__(self):\n        if self.terminal_count:\n            return\
    \ \"({}) [{} ({})]: {}\".format(self.terminal_count, self.item,self.prefix_count,self.next)\n\
    \        else:\n            return \"[{} ({})]: {}\".format(self.item,self.prefix_count,self.next)\n\
    \n    __repr__=__str__\n\nclass Trie_Tree():\n    def __init__(self):\n      \
    \  \"\"\" Trie \u6728\u3092\u751F\u6210\u3059\u308B.\"\"\"\n\n        self.nodes=[Trie_Node(None)]\n\
    \n    def insert(self, S):\n        \"\"\" \u5217 S \u3092\u767B\u9332\u3059\u308B\
    .\n\n        S: \u5217\n        \"\"\"\n        nodes=self.nodes\n        node_id=0\n\
    \        nodes[node_id].prefix_count+=1\n        for x in S:\n            if x\
    \ not in nodes[node_id].next:\n                nodes[node_id].next[x]=len(nodes)\n\
    \                nodes.append(Trie_Node(x))\n            node_id=nodes[node_id].next[x]\n\
    \            nodes[node_id].prefix_count+=1\n        nodes[node_id].terminal_count+=1\n\
    \n    def insert_continuation(self, S, start_id=0):\n        \"\"\" \u5217 S \u3092\
    \u767B\u9332\u3059\u308B. \u305F\u3060\u3057, \u767B\u9332\u306E\u5834\u6240\u306F\
    \ start_id \u304B\u3089\u59CB\u307E\u308B\u3068\u3059\u308B.\n\n        S: \u5217\
    \n        start_id: int\n        \"\"\"\n        nodes=self.nodes\n        node_id=start_id\n\
    \        nodes[node_id].prefix_count+=1\n        for x in S:\n            if x\
    \ not in nodes[node_id].next:\n                nodes[node_id].next[x]=len(nodes)\n\
    \                nodes.append(Trie_Node(x))\n            node_id=nodes[node_id].next[x]\n\
    \            nodes[node_id].prefix_count+=1\n        nodes[node_id].terminal_count+=1\n\
    \n    def count(self, S):\n        \"\"\" \u5217 S \u306E\u6570\u3092\u6C42\u3081\
    \u308B.\n\n        S: \u5217\n        \"\"\"\n        nodes=self.nodes\n     \
    \   node_id=0\n        for x in S:\n            if x not in nodes[node_id].next:\n\
    \                return 0\n            node_id=nodes[node_id].next[x]\n      \
    \  return nodes[node_id].terminal_count\n\n    def count_continuation(self,S,start_id=0):\n\
    \        \"\"\" \u5217 S \u306E\u6570\u3092\u6570\u3048\u308B. \u305F\u3060\u3057\
    , \u691C\u7D22\u306E\u5834\u6240\u306F start_id \u304B\u3089\u59CB\u307E\u308B\
    \u3068\u3059\u308B.\n\n        S: \u5217\n        start_id: int\n        \"\"\"\
    \n        nodes=self.nodes\n        node_id=start_id\n        for x in S:\n  \
    \          if x not in nodes[node_id].next:\n                return 0\n      \
    \      node_id=nodes[node_id].next[x]\n        return nodes[node_id].terminal_count\n\
    \n    def search(self, S):\n        \"\"\" \u5217 S \u304C\u5B58\u5728\u3059\u308B\
    \u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n        S: \u5217\n\
    \        \"\"\"\n        return self.count(S)>0\n\n    def search_continuation(self,S,start_id=0):\n\
    \        \"\"\" \u5217 S \u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\u304B\
    \u3092\u5224\u5B9A\u3059\u308B. \u305F\u3060\u3057, \u691C\u7D22\u306E\u5834\u6240\
    \u306F start_id \u304B\u3089\u59CB\u307E\u308B\u3068\u3059\u308B.\n\n        S:\
    \ \u5217\n        start_id: int\n        \"\"\"\n        return self.count_continuation(S,\
    \ start_id)>0\n\n    def search_prefix(self, S):\n        \"\"\" S \u3092 prefix\
    \ \u306B\u6301\u3064\u5217\u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\u304B\
    \u3092\u5224\u5B9A\u3059\u308B.\n\n        S: \u5217\n        \"\"\"\n       \
    \ nodes=self.nodes\n        node_id=0\n        for x in S:\n            if x not\
    \ in nodes[node_id].next:\n                return False\n            node_id=nodes[node_id].next[x]\n\
    \        return True\n\n    def search_prefix_continuation(self, S, start_id=0):\n\
    \        \"\"\" S \u3092 prefix \u306B\u6301\u3064\u5217\u304C\u5B58\u5728\u3059\
    \u308B\u304B\u3069\u3046\u304B\u3092\u5224\u5B9A\u3059\u308B. \u305F\u3060\u3057\
    , \u691C\u7D22\u306E\u5834\u6240\u306F start_id \u304B\u3089\u59CB\u307E\u308B\
    \u3068\u3059\u308B.\n\n        S: \u5217\n        start_id: int\n        \"\"\"\
    \n        nodes=self.nodes\n        node_id=start_id\n        for x in S:\n  \
    \          if x not in nodes[node_id].next:\n                return False\n  \
    \          node_id=nodes[node_id].next[x]\n        return True\n\n    def __contains__(self,\
    \ S):\n        \"\"\" \u5217 S \u304C\u5B58\u5728\u3059\u308B\u304B\u3069\u3046\
    \u304B\u3092\u5224\u5B9A\u3059\u308B.\n\n        S: \u5217\n        \"\"\"\n \
    \       return self.search(S)\n\n    def count_prefixing(self, S, equal=True):\n\
    \        \"\"\" S \u304C prefix \u306B\u306A\u308B\u3088\u3046\u306A\u5217 (\u524D\
    \ |S| \u9805\u304C S \u306B\u4E00\u81F4\u3059\u308B\u5217) \u306E\u6570\u3092\u6C42\
    \u3081\u308B.\n\n        S: \u5217\n        \"\"\"\n        nodes=self.nodes\n\
    \        node_id=0\n        for x in S:\n            if x not in nodes[node_id].next:\n\
    \                return 0\n            node_id=nodes[node_id].next[x]\n\n    \
    \    N=nodes[node_id]\n        if equal:\n            return N.prefix_count\n\
    \        else:\n            return N.prefix_count-N.terminal_count\n\n    def\
    \ count_prefixing_continuation(self,S,start_id=0):\n        \"\"\" S \u304C prefix\
    \ \u306B\u306A\u308B\u3088\u3046\u306A\u5217\u306E\u6570\u3092\u6C42\u3081\u308B\
    . \u305F\u3060\u3057, \u691C\u7D22\u306E\u5834\u6240\u306F start_id \u304B\u3089\
    \u59CB\u307E\u308B\u3068\u3059\u308B.\n\n        S: \u5217\n        start_id:\
    \ int\n        \"\"\"\n        nodes=self.nodes\n        node_id=start_id\n  \
    \      for x in S:\n            if x not in nodes[node_id].next:\n           \
    \     return 0\n            node_id=nodes[node_id].next[x]\n        return nodes[node_id].prefix_count\n\
    \n    def count_prefixed(self, S, equal=True):\n        \"\"\" S \u3092 prefix\
    \ \u306B\u3059\u308B\u5217 (S=(S[0],...,S[k-1]) \u3068\u3057\u305F\u3068\u304D\
    \u306E\u3042\u308B t \u306B\u304A\u3051\u308B S'=(S[0],...,S[t-1]) ) \u306E\u6570\
    \u3092\u6C42\u3081\u308B.\n\n        S: \u5217\n        \"\"\"\n        nodes=self.nodes\n\
    \        node_id=0\n        count=nodes[node_id].terminal_count\n        for x\
    \ in S:\n            if x not in nodes[node_id].next:\n                return\
    \ count\n            node_id=nodes[node_id].next[x]\n            count+=nodes[node_id].terminal_count\n\
    \n        N=nodes[node_id]\n        if equal:\n            return count\n    \
    \    else:\n            return count-N.terminal_count\n\n    def count_all(self):\n\
    \        \"\"\" \u767B\u9332\u3055\u308C\u3066\u3044\u308B\u5217\u306E\u500B\u6570\
    \u3092\u6C42\u3081\u308B.\n        \"\"\"\n        return self.nodes[0].prefix_count\n\
    \n    def size(self):\n        \"\"\" \u30C8\u30E9\u30A4\u6728\u306B\u304A\u3051\
    \u308B\u9802\u70B9\u6570\u3092\u6C42\u3081\u308B.\n        \"\"\"\n        return\
    \ len(self.nodes)\n\n    def prefix_node_id(self,S):\n        \"\"\" S \u304C\
    \ prefix \u306B\u306A\u308B\u306E\u3092\u62C5\u3046\u9802\u70B9\u306E\u756A\u53F7\
    \u3092\u6C42\u3081\u308B (\u5B58\u5728\u3057\u306A\u3044\u5834\u5408 -1)\n\n \
    \       S: \u5217\n        \"\"\"\n        nodes=self.nodes\n        node_id=0\n\
    \        for x in S:\n            if x not in nodes[node_id].next:\n         \
    \       return -1\n            node_id=nodes[node_id].next[x]\n        return\
    \ node_id\n"
  dependsOn: []
  isVerificationFile: false
  path: Trie.py
  requiredBy: []
  timestamp: '2023-03-18 02:33:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Trie.py
layout: document
redirect_from:
- /library/Trie.py
- /library/Trie.py.html
title: Trie.py
---

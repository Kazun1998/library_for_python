class Trie_Node():
    def __init__(self, item):
        self.item=item
        self.next={}
        self.terminal_count=0
        self.prefix_count=0

    def __str__(self):
        if self.terminal_count:
            return "({}) [{} ({})]: {}".format(self.terminal_count, self.item,self.prefix_count,self.next)
        else:
            return "[{} ({})]: {}".format(self.item,self.prefix_count,self.next)

    __repr__=__str__

class Trie_Tree():
    def __init__(self):
        """ Trie 木を生成する."""

        self.nodes=[Trie_Node(None)]

    def insert(self, S):
        """ 列 S を登録する.

        S: 列
        """
        return self.insert_continuation(S)

    def insert_continuation(self, S, start_id=0):
        """ 列 S を登録する. ただし, 登録の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """
        nodes=self.nodes
        node_id=start_id
        nodes[node_id].prefix_count+=1
        for x in S:
            if x not in nodes[node_id].next:
                nodes[node_id].next[x]=len(nodes)
                nodes.append(Trie_Node(x))
            node_id=nodes[node_id].next[x]
            nodes[node_id].prefix_count+=1
        nodes[node_id].terminal_count+=1

    def count(self, S):
        """ 列 S の数を求める.

        S: 列
        """
        return self.count_continuation(S)

    def count_continuation(self,S,start_id=0):
        """ 列 S の数を数える. ただし, 検索の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """
        nodes=self.nodes
        node_id=start_id
        for x in S:
            if x not in nodes[node_id].next:
                return 0
            node_id=nodes[node_id].next[x]
        return nodes[node_id].terminal_count

    def search(self, S):
        """ 列 S が存在するかどうかを判定する.

        S: 列
        """
        return self.count(S)>0

    def search_continuation(self,S,start_id=0):
        """ 列 S が存在するかどうかを判定する. ただし, 検索の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """
        return self.count_continuation(S, start_id)>0

    def search_prefix(self, S):
        """ S を prefix に持つ列が存在するかどうかを判定する.

        S: 列
        """
        return self.search_prefix_continuation(S)

    def search_prefix_continuation(self, S, start_id=0):
        """ S を prefix に持つ列が存在するかどうかを判定する. ただし, 検索の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """
        nodes=self.nodes
        node_id=start_id
        for x in S:
            if x not in nodes[node_id].next:
                return False
            node_id=nodes[node_id].next[x]
        return True

    def __contains__(self, S):
        """ 列 S が存在するかどうかを判定する.

        S: 列
        """
        return self.search(S)

    def count_prefixing(self, S, equal=True):
        """ S が prefix になるような列 (前 |S| 項が S に一致する列) の数を求める.

        S: 列
        """
        return self.count_prefixing_continuation(S, equal)

    def count_prefixing_continuation(self, S, equal = True, start_id=0):
        """ S が prefix になるような列の数を求める. ただし, 検索の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """

        nodes = self.nodes
        node_id = start_id
        for x in S:
            if x not in nodes[node_id].next:
                return 0
            node_id=nodes[node_id].next[x]

        N = nodes[node_id]
        if equal:
            return N.prefix_count
        else:
            return N.prefix_count - N.terminal_count

    def count_prefixed(self, S, equal=True):
        """ S を prefix にする列 (S=(S[0],...,S[k-1]) としたときのある t における S'=(S[0],...,S[t-1]) ) の数を求める.

        S: 列
        """
        nodes=self.nodes
        node_id=0
        count=nodes[node_id].terminal_count
        for x in S:
            if x not in nodes[node_id].next:
                return count
            node_id=nodes[node_id].next[x]
            count+=nodes[node_id].terminal_count

        N=nodes[node_id]
        if equal:
            return count
        else:
            return count-N.terminal_count

    def count_all(self):
        """ 登録されている列の個数を求める.
        """
        return self.nodes[0].prefix_count

    def size(self):
        """ トライ木における頂点数を求める.
        """
        return len(self.nodes)

    def prefix_node_id(self,S):
        """ S が prefix になるのを担う頂点の番号を求める (存在しない場合 -1)

        S: 列
        """
        nodes=self.nodes
        node_id=0
        for x in S:
            if x not in nodes[node_id].next:
                return -1
            node_id=nodes[node_id].next[x]
        return node_id

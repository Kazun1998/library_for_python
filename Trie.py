class Trie_Node():
    def __init__(self,item):
        self.item=item
        self.next={}
        self.terminal=False
        self.prefix_count=0

    def __str__(self):
        if self.terminal:
            return "*[{} ({})]: {}".format(self.item,self.prefix_count,self.next)
        else:
            return "[{} ({})]: {}".format(self.item,self.prefix_count,self.next)

    __repr__=__str__

class Trie_Tree():
    def __init__(self,artifical_item="@"):
        """ トライ木を生成する.

        artifical_item: 登録される列に登場しないことが保証されている要素
        """
        self.nodes=[Trie_Node(artifical_item)]

    def insert(self,S):
        """ 列 S を登録する.

        S: 列
        """
        nodes=self.nodes
        node_id=0
        nodes[node_id].prefix_count+=1
        for x in S:
            if x not in nodes[node_id].next:
                nodes[node_id].next[x]=len(nodes)
                nodes.append(Trie_Node(x))
            node_id=nodes[node_id].next[x]
            nodes[node_id].prefix_count+=1
        nodes[node_id].terminal=True

    def insert_continuation(self,S,start_id=0):
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
        nodes[node_id].terminal=True

    def search(self,S):
        """ 列 S が存在するかどうかを判定する.

        S: 列
        """
        nodes=self.nodes
        node_id=0
        for x in S:
            if x not in nodes[node_id].next:
                return False
            node_id=nodes[node_id].next[x]
        return nodes[node_id].terminal

    def search_continuation(self,S,start_id=0):
        """ 列 S が存在するかどうかを判定する. ただし, 登録の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """
        nodes=self.nodes
        node_id=start_id
        for x in S:
            if x not in nodes[node_id].next:
                return False
            node_id=nodes[node_id].next[x]
        return nodes[node_id].terminal

    def search_prefix(self,S):
        """ S を prefix に持つ列が存在するかどうかを判定する.

        S: 列
        """
        nodes=self.nodes
        node_id=0
        for x in S:
            if x not in nodes[node_id].next:
                return False
            node_id=nodes[node_id].next[x]
        return True

    def search_prefix_continuation(self,S,start_id=0):
        """ S を prefix に持つ列が存在するかどうかを判定する. ただし, 登録の場所は start_id から始まるとする.

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

    def __contains__(self,S):
        """ 列 S が存在するかどうかを判定する.

        S: 列
        """
        return self.search(S)

    def count_prefix(self,S):
        """ S を prefix に持つ列の個数を求める.

        S: 列
        """
        nodes=self.nodes
        node_id=0
        for x in S:
            if x not in nodes[node_id].next:
                return 0
            node_id=nodes[node_id].next[x]
        return nodes[node_id].prefix_count

    def count_prefix_continuation(self,S,start_id=0):
        """ S を prefix に持つ列の個数を求める. ただし, 登録の場所は start_id から始まるとする.

        S: 列
        start_id: int
        """
        nodes=self.nodes
        node_id=start_id
        for x in S:
            if x not in nodes[node_id].next:
                return 0
            node_id=nodes[node_id].next[x]
        return nodes[node_id].prefix_count

    def count(self):
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

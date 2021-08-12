class Trie_Node():
    def __init__(self,item):
        self.item=item
        self.next={}
        self.terminal=False
        self.prefix_count=0

    def __str__(self):
        if self.terminal:
            return "*[{} [{}]]: {}".format(self.item,self.prefix_count,self.next)
        else:
            return "[{} [{}]]: {}".format(self.item,self.prefix_count,self.next)

    __repr__=__str__

class Trie_Tree():
    def __init__(self,artifical_item="@"):
        self.nodes=[Trie_Node(artifical_item)]

    def insert(self,*S):
        nodes=self.nodes
        node_id=0
        nodes[node_id].prefix_count+=1
        for s in S:
            for x in s:
                if x not in nodes[node_id].next:
                    nodes[node_id].next[x]=len(nodes)
                    nodes.append(Trie_Node(x))
                node_id=nodes[node_id].next[x]
                nodes[node_id].prefix_count+=1
        nodes[node_id].terminal=True

    def search(self,*S):
        nodes=self.nodes
        node_id=0
        for s in S:
            for x in s:
                if x not in nodes[node_id].next:
                    return False
                node_id=nodes[node_id].next[x]
        return nodes[node_id].terminal

    def search_prefix(self,*S):
        nodes=self.nodes
        node_id=0
        for s in S:
            for x in s:
                if x not in nodes[node_id].next:
                    return False
                node_id=nodes[node_id].next[x]
        return True

    def __contains__(self,S):
        return self.search(S)

    def count_prefix(self,*S):
        nodes=self.nodes
        node_id=0
        for s in S:
            for x in s:
                if x not in nodes[node_id].next:
                    return 0
                node_id=nodes[node_id].next[x]
        return nodes[node_id].prefix_count

    def count(self):
        return self.nodes[0].prefix_count()

    def size(self):
        return len(self.nodes)

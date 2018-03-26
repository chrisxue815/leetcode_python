class DefaultDict(dict):
    def __init__(self, default_factory, **kwargs):
        super(DefaultDict, self).__init__(**kwargs)
        self.default_factory = default_factory

    def __missing__(self, key):
        return self.default_factory(key)


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    @staticmethod
    def parse(s):
        nodes = DefaultDict(UndirectedGraphNode)
        for group in s[1:-1].split('#'):
            group = group.split(',')
            label = int(group[0])
            node = nodes[label]
            node.neighbors = [nodes[neighbor] for neighbor in group[1:]]
        return nodes

    def __eq__(self, other):
        def equals(a, b):
            if a.label != b.label or len(a.neighbors) != len(b.neighbors):
                return False
            for a, b in zip(a.neighbors, b.neighbors):
                if not equals(a, b):
                    return False
            return True

        return equals(self, other)

class DisjointSet:
    parent = {}

    def __init__(self, vertices):
        self.vertices = vertices
        for v in vertices:
            self.parent[v] = v

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2

    def output(self):
        ret = {}
        for v in self.vertices:
            ret[self.find(v)] = []

        for v in self.vertices:
            ret[self.find(v)].append(v)

        return [ret[key] for key in ret.keys()]

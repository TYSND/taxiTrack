from Disjoint_set import DisjointSet


class DBPoint:
    type = 0  # 0,1,2 for noise,border,core
    lon, lat = 0, 0
    attr = {}
    neighbor = []

    def __init__(self, lon, lat, attr):
        self.lat = lat
        self.lon = lon
        self.attr = attr

    def dist(self, to):
        return ((to.lon - self.lon) ** 2 + (to.lat - self.lat) ** 2) ** 0.5


class DBScan:
    points = []
    _Eps, _threshold = 0, 0

    def __init__(self, points, Eps, threshold):
        self.points = [self.DBPoint(p.lon, p.lat, p.attr) for p in points]
        self._Eps = Eps
        self._threshold = threshold

    def run(self):
        self.labeling()
        self.denoising()
        return self.assignBorder(self.unionFind())

    def labeling(self):
        for i in range(len(self.points)):
            now = self.points[i]
            for j in range(i + 1, len(self.points)):
                to = self.points[j]
                if now.dist(to) < self._Eps:
                    now.neighbor.append(to)
                    to.neighbor.append(now)

        for p in self.points:
            if len(p.neighbor) > self._threshold:
                p.type = 2  # core
                for nei in p.neighbor:
                    if nei.type != 2:
                        nei.type = 1  # label as border

    def denoising(self):
        for p in self.points:
            if p.type == 0:  # noise
                del p

    def unionFind(self):
        vertices = [p for p in self.points if p.type == 2]  # core only
        ds = DisjointSet(vertices)
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                now, to = vertices[i], vertices[j]
                if now.dist(to) < self._Eps:
                    ds.union(now, to)

        return ds.output()

    def assignBorder(self, coreClusters):
        ret = []
        assigned = {}
        for cores in coreClusters:
            cluster = []
            for core in cores:
                for nei in core.neighbor:
                    if nei.type == 1 and not (nei in assigned):
                        cluster.append(nei)
                        assigned.add(nei)
            cluster.extend(cores)
            ret.append(cluster)
        return ret

class POI:
    lon, lat = 0, 0

    def __init__(self, lon, lat):
        self.lat = lat
        self.lon = lon


class Cluster:
    POIs = []
    left, right = None, None

    def __init__(self,POIs,left=None,right=None):
        self.POIs=POIs
        self.left=left
        self.right=right

    @staticmethod
    def combine(a, b):
        new=Cluster(a.POIs+b.POIs,a,b)
        return new


class HierarchicalClustering:
    dist = {}
    clusters = []
    INF = 1 << 30

    def __init__(self, clusters):
        self.clusters = clusters
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = self.calcDist(clusters[i], clusters[j])
                self.dist[tuple([clusters[i], clusters[j]])] = dist
                self.dist[tuple([clusters[j], clusters[i]])] = dist

    def run(self):
        clusters = self.clusters
        dist = self.dist
        while len(clusters) != 1:
            minDist = self.INF
            toCombine = (0, 1)
            for i in range(len(clusters)):
                for j in range(i + 1, len(clusters)):
                    if dist[tuple([clusters[i], clusters[j]])] < minDist:
                        minDist = dist[tuple([clusters[i], clusters[j]])]
                        toCombine = (i, j)
            i, j = toCombine[0], toCombine[1]
            newCluster = Cluster.combine(clusters[i], clusters[j])
            clusters.append(newCluster)
            self.getCombinedDist(clusters[i], clusters[j], newCluster)
            del clusters[j]
            del clusters[i]
        return clusters[0]

    def getCombinedDist(self, a, b, new):
        pass

    def calcDist(self, a, b):
        pass

from hierarchical_clustering import HierarchicalClustering


class MinHierarchicalClustering(HierarchicalClustering):
    def getCombinedDist(self, a, b, new):
        dist = self.dist
        clusters = self.clusters
        for i in range(len(clusters)):
            if clusters[i] in [a, b, new]:
                continue
            minDist = min(dist[tuple([clusters[i], a])], dist[tuple([clusters[i], b])])
            dist[tuple([clusters[i], new])], dist[tuple([new, clusters[i]])] = minDist,minDist

    def calcDist(self, a, b):
        minDist = self.INF
        for pA in a.POIs:
            for pB in b.POIs:
                minDist = min(((pA.lon - pB.lon) ** 2 + (pA.lat - pB.lat) ** 2) ** 0.5, minDist)
        return minDist

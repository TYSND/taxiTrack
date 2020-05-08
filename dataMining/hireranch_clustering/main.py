from min_hierarchical_clustering import MinHierarchicalClustering
from hierarchical_clustering import POI,Cluster
from write_file import writeFile

if __name__ == '__main__':
    poi = [[0,0], [100,0], [500,0], [600,0], [0,500], [100,500], [500,500], [600,500], ]
    poi=[Cluster([POI(p[0],p[1])]) for p in poi]
    mhc=MinHierarchicalClustering(poi)
    root=mhc.run()
    writeFile(root,"cluster_tree_data.txt")

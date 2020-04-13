## nearestPOI.py by lpjworkroom
## use kd tree of scipy lib
## input array of points and POIs
## return 1.array of distance of neighbours
## 2.array of index of neighbours in kd tree's data

from scipy import spatial


class NearestPOI:
    POI='' #the kd tree
    
    def __init__(self,poi):
        try:
            self.POI=spatial.KDTree(poi)
        except Exception as e:
            print(e)
            print('initialize kdtree with POI failed')

    def query(self,points):
        return self.POI.query(points)



if __name__=='__main__':
    npoi=NearestPOI([[1,2],[3,4],[0,0],[5,3]])
    print(npoi.query([[1,1],[3,4],[23,121]]))

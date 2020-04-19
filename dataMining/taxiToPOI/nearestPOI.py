## nearestPOI.py by lpjworkroom
## use kd tree of scipy lib
## input array of points and POIs
## return 1.array of distance of neighbours
## 2.array of index of neighbours in kd tree's data

from scipy import spatial


class NearestPOI:
    poiData={}
    POI='' #the kd tree
    
    def __init__(self,poiArr):
        for poi in poiArr:
            self.poiData[(poi['lon'],poi['lat'])]=poi
        pointArr=[[poi['lon'],poi['lat']] for poi in poiArr]
        self.POI=spatial.KDTree(pointArr)

    def query(self,points):
        ans=self.POI.query(points)
        ind=ans[1]
        return [self.poiData[tuple(self.POI.data[index])] for index in ind]



if __name__=='__main__':
    npoi=NearestPOI([{'lon':1,'lat':2,'id':'sdf'},{'lon':3,'lat':4,'id':'sdsddf'},
                     {'lon':23,'lat':21,'id':'sdsdfsdfsdff'}])
    print(npoi.query([[1,1],[3,4],[23,121]]))

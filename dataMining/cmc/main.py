from CMC import CMC
from getStampInfo import GetStampInfo

if __name__ == '__main__':
    stampInfo = GetStampInfo()
    timeline = stampInfo.run()
    cmc = CMC(timeline, DBScanPara={'Eps': 0, 'threshold': 0}, life=0, threshold=0)
    cmc = cmc.run()
    for cluster in cmc:
        for poi in cluster.POIs:
            print(poi.attr['id'], end=',')
        print(' from %d to %d' % (cluster.start, cluster.end))

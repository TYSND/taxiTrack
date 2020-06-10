from CMC import CMC
from getStampInfo import GetStampInfo
from DBScan import DBScan
import json
from cluster2Json import cluster2Json
from getCMCInfo import GetCMCInfo


def doCMC():
    stampInfo = GetStampInfo(time=100)
    timeline = stampInfo.run()
    print(len(timeline))

    cmc = CMC(timeline, DBScanPara={'Eps': 10, 'threshold': 2}, life=8, threshold=6)
    cmc = cmc.run()
    for cluster in cmc:
        for poi in cluster.POIs:
            print(poi.attr['id'] + ',')
        print(' from %d to %d' % (cluster.start, cluster.end))

# output:[     //define CMC
#                 {
#                     start:  //CMC start timestamp
#                     end:    //end timestamp
#                     size:,
#                     taxi:[] //id of taxis
#                 }
#              ]
    output=[]
    for cluster in cmc:
        nowCluster={'start':cluster.start,'end':cluster.end,'size':len(cluster.POIs),'taxi':[]}
        for taxi in cluster.POIs:
            nowCluster['taxi'].append(taxi.attr['id'])
        output.append(nowCluster)

    output=GetCMCInfo(output)
    output=output.run()
    with open('CMCdata.json','w') as out:
        out.write(json.dumps(output))


def doDBScan():
    stampInfo = GetStampInfo()
    timeline = stampInfo.run()
    db=DBScan(timeline[0],1000,2)
    db=db.run()
    print('clusters:%d'%len(db))
    with open('data.json','w') as out:
        out.write(cluster2Json(db))


if __name__ == '__main__':
    #doDBScan()
    doCMC()


from random import randint
import json

def randColor():
    color=[randint(0,255) for i in range(3)]
    return {'r':color[0],'g':color[1],'b':color[2]}


def cluster2Json(data):
    ret=[]
    for cluster in data:
        nowCluster=[{'lon':POI.lon,'lat':POI.lat,'type':'leaf'} for POI in cluster]
        ret.append(nowCluster)
    colors=[randColor() for _ in range(len(data))]
    ret={'clusters':ret,'colors':colors}
    return json.dumps(ret)

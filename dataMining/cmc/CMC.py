from DBScan import DBScan
import pprint

pp = pprint.PrettyPrinter(indent=4, depth=3)


class Cluster:
    life, paired = 0, False
    start, end = 0, 0
    POIs = []

    def __init__(self, POIs):
        self.POIs = POIs

    def intersection(self, b):
        aDict = {poi.attr['id']: poi for poi in self.POIs}
        bDict = {poi.attr['id']: poi for poi in b.POIs}

        ret = Cluster([val for id, val in aDict.items() if id in bDict])
        ret.life = self.life
        return ret


class CMC:
    timeline = []  # store POIs in timeline
    DBScan = {'Eps': 0, 'threshold': 0}
    life, threshold = 0, 0

    def __init__(self, timeline, DBScanPara, life, threshold):
        self.timeline = timeline
        self.DBScan = DBScanPara
        self.life = life
        self.threshold = threshold

    def run(self):
        V, ret = [], []
        for ind, POIs in enumerate(self.timeline):
            pp.pprint('CMC now at %d' % ind)
            # pp.pprint('V:')
            # pp.pprint(V)
            print('V:%d' % len(V))

            for v in V:
                v.paired = False

            nxtV = []
            print('DBScan start')
            db = DBScan(POIs, self.DBScan['Eps'], self.DBScan['threshold'])
            clusters = db.run()
            print('DBScan finish')

            print('clusters:%d' % len(clusters))
            # pp.pprint(clusters)
            clusters = [Cluster(cluster) for cluster in clusters]

            for v in V:
                for now in clusters:
                    inter = v.intersection(now)
                    inter.life = v.life + 1
                    if len(inter.POIs) >= self.threshold:
                        nxtV.append(inter)
                        v.paired = now.paired = True

            for v in V:
                if not v.paired and v.life >= self.life:
                    v.end = ind
                    v.start = ind - v.life
                    ret.append(v)

            nxtV.extend([now for now in clusters if not now.paired])

            print('nxtV:%d' % len(nxtV))
            # pp.pprint('nxtV:')
            # pp.pprint(nxtV)
            V = nxtV

        return ret

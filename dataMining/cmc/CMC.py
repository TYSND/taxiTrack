from DBScan import DBPoint, DBScan


class Cluster:
    life, paired = 0, False
    POIs = []

    def __init__(self, POIs):
        self.POIs = POIs

    def intersection(self, b):
        return Cluster([poi for poi in self.POIs if poi in b.POIs])


class CMC:
    timeline = []  # store POIs in timeline
    DBScan = {'Eps': 0, 'threshold': 0}
    life, threshold = 0, 0

    def __init__(self, timeline,DBScanPara,life,threshold):
        self.timeline = timeline
        self.DBScan=DBScanPara
        self.life=life
        self.threshold=threshold

    def run(self):
        V, ret = [], []
        for POIs in self.timeline:
            for v in V:
                v.paired = False

            nxtV = []
            db = DBScan(POIs, self.DBScan['Eps'], self.DBScan['threshold'])
            clusters = db.run()
            clusters = [Cluster(cluster) for cluster in clusters]
            for v in V:
                for now in clusters:
                    inter = v.intersection(now)
                    inter.life = v.life + 1
                    if len(inter) >= self.threshold:
                        nxtV.append(inter)
                        v.paired = now.paired = True

            for v in V:
                if not v.paired and v.life >= self.DBScan['life']:
                    ret.append(v)

            for now in clusters:
                if not now.paired:
                    nxtV.append(now)

        return ret

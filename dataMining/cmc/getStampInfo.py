import pymysql
from DBScan import DBPoint, DBScan


class GetStampInfo:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "a46513", "taxitrack")
        self.cursor = self.db.cursor()

    def run(self):
        ret = []
        for i in range(0, 1439):
            ret.append([])
        sql = "select time_stamp,taxi_id,lon,lat from time_stamp_taxi_info order by time_stamp"
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            for row in results:
                time_stamp = row[0]
                taxi_id = row[1]
                lon = row[2]
                lat = row[3]
                ret[time_stamp].append(DBPoint(lon, lat, {"id": taxi_id}))
        # 打印结果
        # print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
        #	(fname, lname, age, sex, income ))
        # print(ret[0][0].lon,ret[0][0].lat,ret[0][0].attr)
        except Exception as e:
            print("Error:", e)
        self.db.close()
        return ret

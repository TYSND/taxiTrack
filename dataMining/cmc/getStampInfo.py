# -*-coding:utf-8 -*-
import pymysql
from DBScan import DBPoint, DBScan


class GetStampInfo:
    time = 100

    def __init__(self,time=100):
        self.db = pymysql.connect("localhost", "root", "a46513", "taxitrack")
        self.cursor = self.db.cursor()
        self.time=time

    def run(self):
        ret = []
        for i in range(self.time + 1):
            ret.append([])
        sql = "select time_stamp,taxi_id,lon,lat from time_stamp_taxi_info where time_stamp<%d order by time_stamp" % self.time
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            resLen=len(results)
            for ind,row in enumerate(results):
                if ind%10000==0:
                    print("getStampInfo:%d/%d"%(ind,resLen))
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

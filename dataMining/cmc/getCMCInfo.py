# -*-coding:utf-8 -*-
import pymysql
from DBScan import DBPoint, DBScan


# input:
# clusters:[     //define CMC
#                 {
#                     start:  //CMC start timestamp
#                     end:    //end timestamp
#                     size:,
#                     taxi:[] //id of taxis
#                 }
#              ]
# output:
# clusters:[     //define CMC
#                 {
#                     start:  //CMC start timestamp
#                     end:    //end timestamp
#                     size:   //how many points
#                     frames:[    //every point's lon,lat every frame
#                           {
#                               time:,
#                               points:[{id:,lon:,lat:},]
#                           },
#                         ],
#                 }
#              ]
class GetCMCInfo:

    def __init__(self, clusters):
        self.db = pymysql.connect("localhost", "root", "a46513", "taxitrack")
        self.cursor = self.db.cursor()
        self.clusters = clusters

    def run(self):
        ret = []
        for cluster in self.clusters:
            nowCluster = {
                'start': cluster['start'],
                'end': cluster['end'],
                'size': cluster['size'],
                'frames': []
            }
            for time in range(cluster['start'], cluster['end'] + 1):
                nowFrame = {'time': time, 'points': []}
                sql = "select time_stamp,taxi_id,lon,lat from time_stamp_taxi_info where time_stamp=%d " \
                      "and taxi_id in ('%s')" % (time, "','".join(cluster['taxi']))
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
                        nowFrame['points'].append({"id": taxi_id, 'lon': lon, 'lat': lat})
                except Exception as e:
                    print("Error:", e)
                nowCluster['frames'].append(nowFrame)
            ret.append(nowCluster)
        return ret

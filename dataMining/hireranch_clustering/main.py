from min_hierarchical_clustering import MinHierarchicalClustering
from hierarchical_clustering import POI,Cluster
from write_file import writeFile
import pymysql
if __name__ == '__main__':
    poi = []
    db = pymysql.connect("localhost","root","a46513","taxitrack" )
    cursor = db.cursor()
    sql = "select lon,lat from poi_info \
where \
id in (select poi_id from poi_type where poi_type_id = 296) limit 20;"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            lon = row[0]
            lat = row[1]
            poi.append([lon,lat]);
            # 打印结果
            #print ("lon=%d,lat=%d" % (lon,lat ))
    except:
        print ("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    #poi = [[0,0], [100,0], [500,0], [600,0], [0,500], [100,500], [500,500], [600,500], ]
    poi=[Cluster([POI(p[0],p[1])]) for p in poi]
    mhc=MinHierarchicalClustering(poi)
    root=mhc.run()
    writeFile(root,"cluster_tree_data.txt")

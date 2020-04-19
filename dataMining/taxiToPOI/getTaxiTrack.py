#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql


class getTaxiTrack():
	def getTaxiTrack(self):
		db = pymysql.connect("localhost", "root", "a46513", "taxitrack")
		# 使用cursor()方法获取操作游标 
		cursor = db.cursor()

		sql ="select taxi_id from taxi limit 2"
		list=[]
		try:
			# 执行SQL语句
			cursor.execute(sql)
			# 获取1000条出租车id
			taxi_id_results = cursor.fetchall()
			for taxi_id_row in taxi_id_results:
				tid=taxi_id_row[0]
				
				dic = {}
				dic['taxi_id'] = tid
				dic['track'] = []
				
				tracksql="select lon,lat from taxi_info where taxi_id='{taxi_id}'"
				tracksql=tracksql.format(taxi_id=tid)
				#print(tracksql)
				cursor.execute(tracksql)
				track_res = cursor.fetchall()
				for track_row in track_res:
					lon=track_row[0]
					lat=track_row[1]
					tmplist=[lon,lat]
					
					dic['track'].append(tmplist)
				list.append(dic)
			
				
		except pymysql.Error as e:
			print(e.args[0], e.args[1])
		# 关闭数据库连接
		db.close()
		#print(list[0]['taxi_id'])
		print("ok")
		return list
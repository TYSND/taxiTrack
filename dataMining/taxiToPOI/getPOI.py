#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql


class getPOI():
	def getPOI(self):
		db = pymysql.connect("localhost", "root", "a46513", "taxitrack")
		# 使用cursor()方法获取操作游标 
		cursor = db.cursor()

		sql ="select id,poi_name,poi_addr,lon,lat from poi_info"
		list=[]
		try:
			# 执行SQL语句
			cursor.execute(sql)
			# 获取所有记录列表
			results = cursor.fetchall()
			
			for row in results:
				dic={}
				id = row[0]
				poi_name = row[1]
				poi_addr = row[2]
				lon = row[3]
				lat = row[4]
				dic['id']=id
				dic['poi_name']=poi_name
				dic['poi_addr']=poi_addr
				dic['lon']=lon
				dic['lat']=lat
				list.append(dic)
				# 打印结果
				# print ("id=%s,poi_name=%s,poi_addr=%s,lon=%f,lat=%f" % \
				# (id, poi_name, poi_addr, lon, lat ))
				
		except pymysql.Error as e:
			print(e.args[0], e.args[1])
		# 关闭数据库连接
		db.close()

		print("ok")
		return list
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from nearestPOI import NearestPOI 
from getPOI import getPOI 
from getTaxiTrack import getTaxiTrack 

getpoi=getPOI()
poiArr=getpoi.getPOI()
NPOI=NearestPOI(poiArr)
gettaxitrack=getTaxiTrack()
trackArr=gettaxitrack.getTaxiTrack()
print(trackArr)
track=trackArr[0]['track']
trackPOI=NPOI.query(tarck)
print(trackPOI)

#  track2Gpx.py
#  Copyright 2020 lpjworkroom
#  use pygpx lib,convert track data in DB into gpx file format
#  source data must be taxi_info-table-like format in DB
import gpxpy


with open('one_taxi_info.txt','r') as f:
    track={}   #  store taxi track segments list,taxi_id as key
    #  one_taxi_info format:taxi_id,full_load,actual_load,date,lon,lat,attr1,2,3
    for line in f:
        point=line.split(',')
        #  insert taxi point info into dict
        taxi=point[0]
        pointData={'date':point[3],'lon':point[4],'lat':point[5]}
        if taxi in track:
            track[taxi][0].append(pointData)
        else:
            track[taxi]=[[pointData]]
    
    gpx=gpxpy.gpx.GPX()
    for taxi,segments in track.items():
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)
        for seg in segments:
            gpx_segment=gpxpy.gpx.GPXTrackSegment()
            gpx_track.segments.append(gpx_segment)
            for point in seg:
                gpx_segment.points.append(
                    gpxpy.gpx.GPXTrackPoint(point['lat'],point['lon'], elevation=0))
    
    with open('output.gpx','w') as output:
        output.write(gpx.to_xml())

# Design a system which takes in latitude and longiitude and returns back closest 6 locations.

import math
import re

class Point:

  def __init__(self, lat=None, longi=None, coordstr=''):
    if coordstr:
      self.lat, self.longi=self.parsecoords(coordstr)
      return
    self.lat=lat
    self.longi=longi

  def parsecoords(self, coordstr):
    #findall = re.findall('\d+\.?\d*',coordstr)
    reg = re.compile('[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)')
    findall = reg.findall(coordstr)
    print findall
    lat = float(findall[0])
    longi = float(findall[1])
    return lat, longi


  def __str__(self):
    return 'latitude = ' + str(self.lat) + ' longitude = ' + str(self.longi) + '\n'



class Points:

  def __init__(self, points_list=None):
    self.pointslist=[]
    if points_list and points_list[0].__class__.__name__:
      self.pointslist += points_list
    else:
      for coords in points_list:
        self.pointslist.append(Point(coords['lat'], coords['longi']))

  def __str__(self):
    s = 'Points:\n'
    for p in self.pointslist:
      s += '\t' + str(p)
    return s

  def distance(self, point1, point2):
    return(math.sqrt((point1.lat-point2.lat)**2 + (point1.longi-point2.longi)**2))


  def closest(self, to_point, closest_amount=1):
    getkey = lambda other_point: self.distance(to_point, other_point)
    return Points(sorted(self.pointslist, key=getkey)[:closest_amount])



points=[Point(0,0), Point(0,1), Point(0,3), Point(15,0), Point(15,15), Point(10,10), Point(0,1), Point(2,2), Point(5,5)]

given_point=Point(5,5)

#print(p1.distance(p2))

pnts=Points(points)

closest=pnts.closest(given_point, 5)

print closest


strp=Point(coordstr='-345897, +43587.430857')

print strp

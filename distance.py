# -*- coding: utf-8 -*-
from math import sqrt
from math import cos
from math import sin
import math

def rad(d):
    return d * math.pi / 180.0

def getDistance(lat1, lng1, lat2, lng2):
    EARTH_REDIUS = 6378.137
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    print("distance=", s)
    return s

if __name__ == '__main__':
# 1中央大學 2永安漁港
    lat1 = 24.961656
    lng1 = 121.215133
    lat2 = 24.991766
    lng2 = 121.014290
    getDistance(lat1, lng1, lat2, lng2)


# 參考網站 https://www.twblogs.net/a/5c19c02abd9eee5e41848d48
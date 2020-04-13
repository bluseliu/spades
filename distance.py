# -*- coding: utf-8 -*-
from math import sqrt
from math import cos
from math import sin
import math

def rad(d):
    return d * math.pi / 180.0

def getDistance_A(lat1, lng1, lat2, lng2):
    EARTH_REDIUS = 6378.137
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s_A = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b / 2), 2)))
    s_A = s_A * EARTH_REDIUS
    print("distance_A =", s_A)
    return s_A

def getDistance_B(lat1, lng1, lat3, lng3):
    EARTH_REDIUS = 6378.137
    radLat1 = rad(lat1)
    radLat3 = rad(lat3)
    a = radLat1 - radLat3
    b = rad(lng1) - rad(lng3)
    s_B = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat3) * math.pow(sin(b / 2), 2)))
    s_B = s_B * EARTH_REDIUS
    print("distance_B =", s_B)
    return s_B

def getDistance_C(lat1, lng1, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat1 = rad(lat1)
    radLat4 = rad(lat4)
    a = radLat1 - radLat4
    b = rad(lng1) - rad(lng4)
    s_C = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_C = s_C * EARTH_REDIUS
    print("distance_C =", s_C)
    return s_C

if __name__ == '__main__':
# 1中央大學 2永安漁港 3向陽農場 4.湖口老街
    lat1 = 24.961656
    lng1 = 121.215133
    lat2 = 24.991766
    lng2 = 121.014290
    lat3 = 25.008022
    lng3 = 121.111452
    lat4 = 24.877548
    lng4 = 121.056787

getDistance_A(lat1, lng1, lat2, lng2)
getDistance_B(lat1, lng1, lat3, lng3)
getDistance_C(lat1, lng1, lat4, lng4)


# 參考網站 https://www.twblogs.net/a/5c19c02abd9eee5e41848d48
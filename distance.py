# -*- coding: utf-8 -*-
from math import sqrt
from math import cos
from math import sin
import math

EARTH_REDIUS = 6378.137

# 1中央大學 2觀音草漯沙丘 3向陽農場 4永安漁港
lat_all = [24.961656, 25.07825, 25.008022, 24.991766]
lat_len = len(lat_all)
print(lat_len)

lng_all = [121.215133, 121.125950, 121.111452, 121.01429]
lat_len = len(lng_all)

for lat in lat_all:
    radLat1 = lat_all[0] * math.pi / 180.0



radLat2 = lat_all[1] * math.pi / 180.0
a = radLat1 - radLat2
b = (lng_all[0] * math.pi / 180.0) - (lng_all[1] * math.pi / 180.0)
s_1to2 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b / 2), 2)))
s_1to2 = s_1to2 * EARTH_REDIUS
print("distance_1to2 =", s_1to2)




"""
def getDistance_1to3(lat1, lng1, lat3, lng3):
    EARTH_REDIUS = 6378.137
    radLat1 = lat1 * math.pi / 180.0
    radLat3 = lat3 * math.pi / 180.0
    a = radLat1 - radLat3
    b = (lng1 * math.pi / 180.0) - (lng3 * math.pi / 180.0)
    s_1to3 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat3) * math.pow(sin(b / 2), 2)))
    s_1to3 = s_1to3 * EARTH_REDIUS
    print("distance_1to3 =", s_1to3)
    return s_1to3

def getDistance_1to4(lat1, lng1, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat1 = lat1 * math.pi / 180.0
    radLat4 = lat4 * math.pi / 180.0
    a = radLat1 - radLat4
    b = (lng1 * math.pi / 180.0) - (lng4 * math.pi / 180.0)
    s_1to4 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_1to4 = s_1to4 * EARTH_REDIUS
    print("distance_1to4 =", s_1to4)
    return s_1to4


def getDistance_2to3(lat2, lng2, lat3, lng3):
    EARTH_REDIUS = 6378.137
    radLat2 = lat2 * math.pi / 180.0
    radLat3 = lat3 * math.pi / 180.0
    a = radLat2 - radLat3
    b = (lng2 * math.pi / 180.0) - (lng3 * math.pi / 180.0)
    s_2to3 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat2) * cos(radLat3) * math.pow(sin(b / 2), 2)))
    s_2to3 = s_2to3 * EARTH_REDIUS
    print("distance_2to3 =", s_2to3)
    return s_2to3

def getDistance_2to4(lat2, lng2, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat2 = lat2 * math.pi / 180.0
    radLat4 = lat4 * math.pi / 180.0
    a = radLat2 - radLat4
    b = (lng2 * math.pi / 180.0) - (lng4 * math.pi / 180.0)
    s_2to4 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat2) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_2to4 = s_2to4 * EARTH_REDIUS
    print("distance_2to4 =", s_2to4)
    return s_2to4

def getDistance_3to4(lat3, lng3, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat3 = lat3 * math.pi / 180.0
    radLat4 = lat4 * math.pi / 180.0
    a = radLat3 - radLat4
    b = (lng3 * math.pi / 180.0) - (lng4 * math.pi / 180.0)
    s_3to4 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat3) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_3to4 = s_3to4 * EARTH_REDIUS
    print("distance_3to4 =", s_3to4)
    return s_3to4




A_B = round(getDistance_1to2(lat1, lng1, lat2, lng2),1)
A_C = round(getDistance_1to3(lat1, lng1, lat3, lng3),1)
A_D = round(getDistance_1to4(lat1, lng1, lat4, lng4),1)
B_C = round(getDistance_2to3(lat2, lng2, lat3, lng3),1)
B_D = round(getDistance_2to4(lat2, lng2, lat4, lng4),1)
C_D = round(getDistance_3to4(lat3, lng3, lat4, lng4),1)

route_1 = A_B + B_C + C_D ; print('route_1 A-B-C-D:', route_1)
route_2 = A_B + B_D + C_D ; print('route_2 A-B-D-C:', route_2)
route_3 = A_C + B_C + B_D ; print('route_3 A-C-B-D:', route_3)
route_4 = A_C + C_D + B_D ; print('route_4 A-C-D-B:', route_4)
route_5 = A_D + B_D + B_C ; print('route_4 A-D-B-C:', route_5)
route_6 = A_D + C_D + B_C ; print('route_4 A-D-C-B:', route_6)
print()
print('=== > Suggest route is:', min(route_1, route_2, route_3, route_4, route_5, route_6))

# 參考網站 https://www.twblogs.net/a/5c19c02abd9eee5e41848d48

"""
"""
# ===================================
# -*- coding: utf-8 -*-
from math import sqrt
from math import cos
from math import sin
import math

def getDistance_1to2(lat1, lng1, lat2, lng2):
    EARTH_REDIUS = 6378.137
    radLat1 = lat1 * math.pi / 180.0
    radLat2 = lat2 * math.pi / 180.0
    a = radLat1 - radLat2
    b = (lng1* math.pi / 180.0) - (lng2 * math.pi / 180.0)
    s_1to2 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b / 2), 2)))
    s_1to2 = s_1to2 * EARTH_REDIUS
    print("distance_1to2 =", s_1to2)
    return s_1to2

def getDistance_1to3(lat1, lng1, lat3, lng3):
    EARTH_REDIUS = 6378.137
    radLat1 = lat1 * math.pi / 180.0
    radLat3 = lat3 * math.pi / 180.0
    a = radLat1 - radLat3
    b = (lng1 * math.pi / 180.0) - (lng3 * math.pi / 180.0)
    s_1to3 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat3) * math.pow(sin(b / 2), 2)))
    s_1to3 = s_1to3 * EARTH_REDIUS
    print("distance_1to3 =", s_1to3)
    return s_1to3

def getDistance_1to4(lat1, lng1, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat1 = lat1 * math.pi / 180.0
    radLat4 = lat4 * math.pi / 180.0
    a = radLat1 - radLat4
    b = (lng1 * math.pi / 180.0) - (lng4 * math.pi / 180.0)
    s_1to4 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_1to4 = s_1to4 * EARTH_REDIUS
    print("distance_1to4 =", s_1to4)
    return s_1to4


def getDistance_2to3(lat2, lng2, lat3, lng3):
    EARTH_REDIUS = 6378.137
    radLat2 = lat2 * math.pi / 180.0
    radLat3 = lat3 * math.pi / 180.0
    a = radLat2 - radLat3
    b = (lng2 * math.pi / 180.0) - (lng3 * math.pi / 180.0)
    s_2to3 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat2) * cos(radLat3) * math.pow(sin(b / 2), 2)))
    s_2to3 = s_2to3 * EARTH_REDIUS
    print("distance_2to3 =", s_2to3)
    return s_2to3

def getDistance_2to4(lat2, lng2, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat2 = lat2 * math.pi / 180.0
    radLat4 = lat4 * math.pi / 180.0
    a = radLat2 - radLat4
    b = (lng2 * math.pi / 180.0) - (lng4 * math.pi / 180.0)
    s_2to4 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat2) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_2to4 = s_2to4 * EARTH_REDIUS
    print("distance_2to4 =", s_2to4)
    return s_2to4

def getDistance_3to4(lat3, lng3, lat4, lng4):
    EARTH_REDIUS = 6378.137
    radLat3 = lat3 * math.pi / 180.0
    radLat4 = lat4 * math.pi / 180.0
    a = radLat3 - radLat4
    b = (lng3 * math.pi / 180.0) - (lng4 * math.pi / 180.0)
    s_3to4 = 2 * math.asin(math.sqrt(math.pow(sin(a / 2), 2) + cos(radLat3) * cos(radLat4) * math.pow(sin(b / 2), 2)))
    s_3to4 = s_3to4 * EARTH_REDIUS
    print("distance_3to4 =", s_3to4)
    return s_3to4

if __name__ == '__main__':
# 1中央大學 2觀音草漯沙丘 3向陽農場 4永安漁港
    lat1 = 24.961656
    lng1 = 121.215133
    lat2 = 25.078259
    lng2 = 121.125950
    lat3 = 25.008022
    lng3 = 121.111452
    lat4 = 24.991766
    lng4 = 121.014290


A_B = round(getDistance_1to2(lat1, lng1, lat2, lng2),1)
A_C = round(getDistance_1to3(lat1, lng1, lat3, lng3),1)
A_D = round(getDistance_1to4(lat1, lng1, lat4, lng4),1)
B_C = round(getDistance_2to3(lat2, lng2, lat3, lng3),1)
B_D = round(getDistance_2to4(lat2, lng2, lat4, lng4),1)
C_D = round(getDistance_3to4(lat3, lng3, lat4, lng4),1)

route_1 = A_B + B_C + C_D ; print('route_1 A-B-C-D:', route_1)
route_2 = A_B + B_D + C_D ; print('route_2 A-B-D-C:', route_2)
route_3 = A_C + B_C + B_D ; print('route_3 A-C-B-D:', route_3)
route_4 = A_C + C_D + B_D ; print('route_4 A-C-D-B:', route_4)
route_5 = A_D + B_D + B_C ; print('route_4 A-D-B-C:', route_5)
route_6 = A_D + C_D + B_C ; print('route_4 A-D-C-B:', route_6)
print()
print('=== > Suggest route is:', min(route_1, route_2, route_3, route_4, route_5, route_6))

# 參考網站 https://www.twblogs.net/a/5c19c02abd9eee5e41848d48
"""
 # -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:42:07 2019

@author: Yekta
"""
# filtered= [[137, 233], [154, 217], [167, 202], [176, 188], [189, 174], [207, 161], [209, 147], [223, 135], [230, 123], [239, 110], [253, 101], [261, 89], [270, 78], [277, 67], [281, 54], [298, 48], [304, 36], [318, 30], [323, 18], [337, 13], [352, 8], [363, 1], [382, 2], [397, 0], [419, 5], [435, 6], [448, 5], [463, 8], [476, 8], [490, 11], [500, 11], [510, 9], [521, 11], [532, 13], [540, 11], [550, 14], [558, 13], [566, 12], [574, 11], [582, 12], [590, 13], [598, 14], [606, 16], [614, 17], [621, 17], [627, 13], [635, 19], [642, 21], [649, 24], [655, 20], [662, 23], [669, 25], [675, 26], [682, 22], [689, 22], [695, 24], [702, 21], [709, 22], [717, 17], [724, 20], [731, 20], [740, 17], [746, 22], [755, 20], [762, 20], [771, 20], [780, 19], [786, 23], [800, 16], [808, 18], [815, 23], [825, 23], [834, 25], [843, 29], [847, 37], [854, 41], [858, 49], [867, 53], [870, 61], [878, 66], [880, 75], [891, 78], [898, 84], [904, 90], [906, 99], [915, 105], [920, 112], [928, 118], [933, 126], [939, 134], [944, 142], [948, 150], [954, 159], [960, 167], [969, 175], [974, 184], [985, 193], [989, 203], [1000, 212], [1007, 223], [1019, 233], [1031, 245], [1036, 257], [1044, 270], [1058, 283], [1073, 299], [1087, 315], [1107, 333], [1122, 352], [1136, 371], [1147, 391], [1157, 412], [1155, 429], [1156, 447], [1159, 467], [1152, 483], [1151, 502], [1141, 516], [1140, 537], [1132, 553], [1126, 571], [1118, 587], [1115, 608], [1108, 626], [1104, 648], [1093, 665], [1084, 682], [1078, 705], [1074, 731], [1062, 749], [1054, 773], [1045, 797], [1018, 880], [996, 889], [983, 916], [967, 939], [945, 949], [926, 966], [905, 981], [883, 995], [860, 1005], [835, 1009], [813, 1027], [604, 602], [595, 583], [588, 563], [577, 564], [565, 567], [547, 586], [528, 607], [162, 921], [147, 897], [116, 894], [97, 874], [79, 817], [64, 795], [78, 749], [63, 729], [64, 668], [55, 646], [40, 628], [21, 613], [34, 579], [29, 556], [27, 532], [12, 515], [0, 496], [21, 464], [14, 444], [20, 420], [33, 395], [43, 372], [57, 349], [70, 327], [82, 307], [95, 287], [108, 268], [119, 250], [109, 251], [90, 269], [77, 287], [65, 307], [49, 328], [38, 349], [24, 372], [14, 395], [6, 419], [11, 440], [15, 461], [0, 489], [7, 510], [9, 533], [31, 548], [32, 572], [26, 600], [48, 614], [16, 690], [33, 708], [46, 829], [68, 845], [75, 876], [96, 893], [124, 901], [148, 914], [163, 938], [504, 618], [525, 598], [545, 576], [557, 576], [567, 579], [575, 592], [581, 615], [740, 1067], [764, 1056], [787, 1036], [811, 1028], [835, 1023], [879, 996], [897, 972], [923, 974], [941, 953], [956, 929], [975, 915], [988, 889], [1001, 866], [1010, 838], [1020, 815], [1038, 803], [1042, 772], [1049, 749], [1058, 729], [1061, 703], [1070, 685], [1082, 670], [1084, 646], [1096, 633], [1106, 618], [1112, 599], [1121, 584], [1126, 566], [1139, 553], [1132, 528], [1140, 513], [1148, 498], [1144, 477], [1141, 458], [1139, 439], [1129, 419], [1117, 398], [1105, 379], [1087, 359], [1067, 341], [1056, 326], [1048, 312], [1035, 298], [1029, 285], [1018, 273], [1009, 261], [1000, 251], [998, 240], [989, 230], [975, 221], [975, 211], [965, 203], [961, 194], [951, 186], [949, 177], [945, 169], [941, 160], [936, 152], [928, 145], [920, 139], [916, 131], [914, 123], [908, 116], [898, 111], [894, 104], [887, 98], [880, 92], [878, 83], [873, 77], [869, 68], [861, 64], [855, 58], [848, 53], [839, 50], [830, 48], [821, 47], [811, 47], [801, 47], [793, 45], [785, 43], [777, 42], [769, 42], [761, 42], [754, 39], [744, 43], [737, 44], [731, 39], [723, 43], [716, 43], [708, 45], [703, 39], [696, 39], [689, 41], [682, 42], [676, 41], [669, 39], [662, 37], [656, 35], [649, 33], [642, 31], [635, 31], [628, 31], [620, 31], [613, 29], [605, 27], [597, 26], [588, 21], [580, 22], [573, 24], [563, 21], [555, 23], [546, 22], [537, 22], [527, 22], [516, 20], [502, 15], [490, 13], [478, 13], [464, 10], [452, 12], [432, 5], [414, 2], [396, 0], [381, 3], [364, 4], [350, 8], [338, 15], [331, 25], [320, 34], [309, 41], [296, 49], [289, 60], [277, 69], [272, 82], [264, 93], [248, 101], [242, 114], [227, 124], [217, 136], [200, 147], [196, 162], [173, 173], [162, 187], [154, 202], [143, 218], [125, 234]]

from __future__ import print_function
import numpy as np
#import borderYekta
import yeniMotor
import yeniMotorFirst
import time
import encoderemre
import copy
import csv
import threading
import ultra
import polar2cart
from landmarkExtraction import landmarkExtraction
import did_I_see
import kosma4unEdit
import dolasma_main
import matplotlib
from matplotlib import pyplot as plt
import math


olcum=[]
pointCld=[]
robotLoc=[0,0,90] # [x,y,rotation]
objMtx=[]

#Ilk tarama
[pointCld,objMtx]=yeniMotorFirst.scan(robotLoc,pointCld,objMtx) #pointCld cartesian şu an
time.sleep(0.01)
oldXY=pointCld

#closest=objeler[0].index(min(objeler[0]))
a=1

while (a==1):
    objeDist=min([(((x[0]-robotLoc[0])**2)+((x[1]-robotLoc[1])**2)),x] for x in objMtx if x[2]==0)
    print('objeDist=',objeDist)
    destination=[objeDist[1][0],objeDist[1][1]]
    print('destination=',destination)
     #robotLoc=encoderemre.gosh(robotLoc,[destination])

    objMtx[objMtx.index(objeDist[1])][2]=1
    pathList=kosma4unEdit.runForest(pointCld,robotLoc,destination)
    print('pathlist=',pathList)
    robotLoc=encoderemre.gosh(robotLoc,pathList)
    robotLoc=encoderemre.gtime(robotLoc,(math.degrees(math.atan2((destination[1]-robotLoc[1]),(destination[0]-robotLoc[0])))-robotLoc[2]),0)
    [pointCld,objMtx]=yeniMotorFirst.scan(robotLoc,pointCld,objMtx)
    oldXY=pointCld
    pointCld,robotLoc,objMtx,oldXY=dolasma_main.scanObj(pointCld,robotLoc,objMtx,oldXY)
     ##etrafında dolaş. Dolaşacağı objeyi 1 le eşitle


    print("harito",pointCld)

    
    xler=[]
    yler=[]
    for i in pointCld:
        xler.append(i[0])
        yler.append(i[1])
#plt.scatter(xler,yler)
#plt.show()
    with open( '/home/pi/Desktop/harito.csv','w',newline='') as myfile:
        wr=csv.writer(myfile)
        wr.writerows(pointCld)
    print('objMtx Kontrol=',objMtx)
    for tam in objMtx:
        af=[]
        if tam[2]==0:
            af.append(tam)
            break
        else:
            continue
            print('bitiyor')
    if(len(af)==0):
        a=0
    else:
        a=1
#dummy=borderYekta.harita(pointCld)
print(pointCld)    
    
xler=[]
yler=[]
for i in pointCld:
    xler.append(i[0])
    yler.append(i[1])
#plt.scatter(xler,yler)
#plt.show()
with open( './kare2.csv','w',newline='') as myfile:
	wr=csv.writer(myfile)
	wr.writerows(pointCld)


print("bitti")








from random import randrange

from matplotlib import pyplot as plt
from matplotlib.axis import Axis

# Structure of Classification of Student datapoints
    # 1. ID of student
    # 2. Class of ID
    # 3. X Axis Value
    # 4. Y Axis Value

class_std = [
         ["t1","Good"      , 10, 61],
         ["t2","Good"      , 29, 80],   
         ["t3","Excellent" , 40, 80],
         ["t4","Excellent" , 60, 80],          
         ["t5","Poor"      , 20, 39],
         ["t6","Poor"      , 39, 20],           
         ["t7","Average"   , 61, 20],
         ["t8","Average"   , 80, 39],           
         ["t9","Special"   , 71, 80],
         ["t0","Special"   , 90, 61],  
# ##
         [  1,"Special"   , 78,  82],
         [  2,"Excellent" , 36, 99],
         [  3,"Excellent" , 57, 61],
         [  4,"Special"   , 81, 73],
         [  5,"Good"      ,  9, 73],
         [  6,"Excellent" , 59, 78],
         [  7,"Special"   , 84, 67],
         [  8,"Good"      , 28, 75],
         [  9,"Poor"      , 24, 29],
         [ 10,"Excellent" , 53, 89],
         [ 11,"Good"      , 10, 85],
         [ 12,"Good"      , 17, 98],
         [ 13,"Excellent" , 56, 78],
# 14
# 15
         [ 16,"Special"   , 74, 63],
         [ 17,"Good"      , 21, 63],
         [ 18,"Excellent" , 63, 89],
 
         [ 20,"Poor"      , 29, 15],
         [ 21,"Good"      , 13, 90],
         [ 22,"Poor"      ,  1 , 0],
         [ 23,"Good"      , 22, 89],
         [ 24,"Poor"      ,  3, 35],
         [ 25,"Excellent" , 37, 80],
         [ 26,"Poor"      , 27,  1],
         [ 27,"Excellent" , 30, 74],
# 28
         [ 29,"Excellent" , 38, 81],
# 30
         [ 31,"Average"   , 72, 10],
         [ 32,"Excellent" , 53, 77],
         [ 33,"Average"   , 99, 20],
         [ 34,"Excellent" , 63, 60],
         [ 35,"Good"      , 23, 69],
         [ 36,"Average"   , 77, 36],
         [ 37,"Average"   , 89, 28],
         [ 38,"Good"      , 29, 64],
         [ 39,"Excellent" , 38, 70],
         [ 40,"Excellent" , 53, 63],
         [ 41,"Special"   , 75, 76],
         [ 42,"Poor"      , 31, 30],
         [ 43,"Excellent" , 50, 89],
         [ 44,"Special"   , 73, 78],
         [ 45,"Excellent" , 30, 65],
# 46
# 47
         [ 48,"Excellent", 36, 74],
         [ 49,"Excellent", 40, 78],
# 50
         [ 51,"Excellent", 44, 72],
         [ 52,"Special"  , 84, 71]
        ]

std_name = {
             1:"aa",
             2:"ab",
             3:"ac",
             4:"ad",
             5:"ae",
             6:"af",
             7:"ag",
             8:"ah",
             9:"ai",
            10:"aj",
            11:"ak",
            12:"al",
            13:"am",
            14:"an",
            15:"ao",
            16:"ap",
            17:"aq",
            18:"ar",
            19:"as",
            20:"at",
            21:"au",
            22:"av",
            23:"aw",
            24:"ax",
            25:"ay",
            26:"az",
            27:"ba",
            28:"bb",
            29:"bc",
            30:"bd",
            31:"be",
            32:"bf",
            33:"bg",
            34:"bh",
            35:"bi",
            36:"bj",
            37:"bk",
            38:"bl",
            39:"bm",
            40:"bn",
            41:"bo",
            42:"bp",
            43:"bq",
            44:"br",
            45:"bs",
            46:"bt",
            47:"bu",
            48:"bv",
            49:"bw",
            50:"bx",
            51:"by",
            52:"bz",
           }


std_prop = {
            "Good":[],
            "Good":[],            
            "Excellent":[],
            "Excellent":[],            
            "Poor":[],
            "Poor":[],            
            "Average":[],
            "Average":[],            
            "Special":[],
            "Special":[],            
             1:[70, 85, 78, 70, 1143 ],
             2:[75, 26, 7, 100, 1438],
             3:[81, 29, 60, 35, 661],
             4:[94, 73, 76, 63, 559],
             5:[75, 57, 73, 87, 93],
             6:[19, 70, 86, 70, 634],
             7:[77, 98, 77, 38, 1326],
             8:[42, 67, 94, 51, 1640],
             9:[30, 20, 80, 63, 1285],
            10:[73, 9, 75, 79, 1728 ],
            11:[34, 7, 79, 85, 622  ],
            12:[94, 48, 27, 98, 1581],
            13:[92, 50, 26, 65, 933 ],
            14:[5, 9, 32, 14, 1411  ],
            15:[71, 3, 94, 10, 110  ],
            16:[96, 78, 47, 29, 1471],
            17:[2, 12, 48, 33, 1010 ],
            18:[85, 16, 86, 78, 1641],
            19:[79, 48, 10, 55, 72  ],
            20:[66, 24, 55, 92, 1538],
            21:[54, 54, 67, 91, 759 ],
            22:[58, 73, 34, 77, 33  ],
            23:[59, 36, 80, 83, 1181],
            24:[42, 91, 38, 70, 1372],
            25:[13, 2, 95, 93, 165  ],
            26:[92, 71, 37, 44, 1417],
            27:[75, 13, 1, 60, 750  ],
            28:[31, 23, 83, 19, 1069],
            29:[1, 78, 35, 76, 685  ],
            30:[6, 71, 46, 1, 42    ],
            31:[94, 13, 79, 40, 416 ],
            32:[13, 61, 83, 58, 1331],
            33:[80, 33, 30, 68, 404 ],
            34:[70, 64, 53, 54, 171 ],
            35:[16, 49, 4, 56, 511  ],
            36:[33, 80, 26, 59, 1037],
            37:[34, 27, 84, 83, 1095],
            38:[18, 40, 27, 34, 1164],
            39:[15, 11, 88, 62, 373 ],
            40:[68, 8, 81, 34, 1062 ],
            41:[50, 80, 94, 53, 1669],
            42:[3, 62, 27, 17, 34   ],
            43:[2, 68, 79, 79, 1557 ],
            44:[96, 89, 33, 92, 149 ],
            45:[75, 10, 3, 79, 56   ],
            46:[91, 6, 33, 42, 47   ],
            47:[49, 54, 8, 57, 1027 ],
            48:[19, 87, 0, 51, 1327 ],
            49:[94, 13, 13, 93, 136 ],
            50:[1, 7, 16, 4, 11 ],
            51:[18, 20, 93, 46, 1528],
            52:[71, 91, 90, 64, 395 ],
           }

def change_prop():
    for i in range(1,52+1):
        o = [randrange(0,101),randrange(0,101),randrange(0,101),randrange(0,101),randrange(0,1801)]
        std_prop[i] = o
    print(std_prop)
# change_prop()

def classify_statically():
    for i in class_std:
        x,y = i[2],i[3]
        print(i[0],end=" ")
        if(y in range(60,101) and x in range(0,30)):
            print("\"Good\"")
        elif(y in range(60,101) and x in range(30,70)):
            print("\"Excellent\"")
        elif(y in range(60,101) and x in range(70,101)):
            print("\"Special\"")
        elif(y in range(0,40) and x in range(0,40)):
            print("\"Poor\"")
        elif(y in range(0,40) and x in range(60,101)):
            print("\"Average\"")

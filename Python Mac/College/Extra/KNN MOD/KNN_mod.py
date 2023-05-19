from collections import Counter
from math import ceil, log10, sqrt

import KNN_DataSet_mod
import matplotlib.pyplot as plt
from matplotlib.axis import Axis

std_prop = KNN_DataSet_mod.std_prop
class_std = KNN_DataSet_mod.class_std

# The new_std Dict's stucture is given by
#     Key Student ID 
#     1. Internal marks Percentage
#     2. External marks Percentage
#     3. Attendance Percentage
#     4. Teacher Likeablity (100)
#     5. Awards and certificate[max 1800]

def calc_coord(new_std : list) -> tuple :
    """ This function takes the value of properties of the new student and returns its coordinate on a 100x100 unit plane """
    
    # This is the fomula for calculating the value of x axis
    form_x = (new_std[0] + new_std[1] + new_std[2])/3

    # This function reduces the value of number of certificates to around the range of 0:100
    o = 33*log10(new_std[4]+1) - 8

    if(new_std[4]<=0): o=0
    elif(new_std[4]==1): o=1
    form_y = (o + new_std[3])/2

    return (ceil(form_x),ceil(form_y))


def create_dataset():
    """ This function takes the ID of students and xy values of the student and puts them in a list """
    class_std = []
    for i,v in std_prop.items():
        o = [i]
        o.extend(calc_coord(v))
        class_std.append(o)

    print(class_std)
# create_dataset()

def plot(class_std : list ) -> None:
    """ The data present in the database is plotted on to the graph of 100X100 plane """
    class_std= [[class_std[j][i] for j in range(len(class_std))] for i in range(len(class_std[0]))]

    fig, ax = plt.subplots() 
    ax.scatter(class_std[2],class_std[3])
    # plt.title(i[0])
    Axis.set(ax, xlabel ='X-Axis', ylabel ='Y-Axis',  
                xlim =(0,100), ylim =(0, 100))

    ax.grid()
    plt.show()
# plot()

def plot_indi_iter(std : list ) -> None:
    """ The data present in the database is plotted on to the graph of 100X100 plane one datapoint at time """
    for s in std:
        fig, ax = plt.subplots() 
        ax.scatter(s[2],s[3])
        plt.title(s[0])
        Axis.set(ax, xlabel ='X-Axis', ylabel ='Y-Axis',  
                    xlim =(0,100), ylim =(0, 100))

        ax.grid()
        plt.show()

def plot_indi(s : list ) -> None:
    """ The data present in the database is plotted on to the graph of 100X100 plane one datapoint at time """
    

    fig, ax = plt.subplots() 
    ax.scatter(s[2],s[3])
    plt.title(s[0])
    Axis.set(ax, xlabel ='X-Axis', ylabel ='Y-Axis',  
                xlim =(0,100), ylim =(0, 100))

    ax.grid()
    plt.show()


def calc_dist(i,j,x,y) -> int:
    """ Returns the eucledian distance from different points """
    return ceil(sqrt((x-i)**2+(y-j)**2))



# The students that are needed to be used in the algorithm
# 14: Good     , Ex : Good,
# 15: Average  , Ex : Average,
# 19: Excellent, Ex : Excellent,
# 28: Excellent, Ex : Excellent,
# 30: Poor     , Ex : Poor,
# 46: Excellent, Ex : Excellent,
# 47: Excellent, Ex : Excellent,
# 50: Poor     , Ex : Poor 


# Core Algorithm
def KNN(no_of_neibour : int, new_std : list, class_std : list):
    """ Returns the class of the student be checking its K neibours nearest to the student on the base of its property """
    xfac,yfac = calc_coord(new_std)
    k = no_of_neibour
    temp = []
    for x in class_std:
        _,c,i,j = x
        dist = calc_dist(i,j,xfac,yfac)


        if len(temp)<k:
            temp.append([c,i,j,dist])
            temp.sort(key= lambda x: x[3])

        else :
            for x in range(k):
                if(temp[x][3]>dist):
                    temp[x] = [c,i,j,dist]
                    break
    
    class_name = []
    for i in temp: class_name.append(i[0])

    freq_dict = dict(Counter(class_name)).items()
    # print(freq_dict)
    b = max(list(freq_dict),key= lambda x: x[1])
    print(b[0])


#                                        Plot the whole class on plane
# plot(class_std)




#                       Plot the student with ID which is intentionally not put into class
# ID_std = 1
# KNN(5,std_prop[ID_std],class_std)
# plot_indi([ID_std,"",calc_coord(std_prop[ID_std])[0],calc_coord(std_prop[ID_std])[1]])
            
plot_indi(std_prop[1])

#                                      Plot the student with new property 
# std = [80,80,80,70,230]
# KNN(5,std,class_std)
# o = ["",'']
# o.extend(calc_coord(std))
# plot_indi(o)





















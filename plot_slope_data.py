from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

def calc_slope(start, end, run):
    rise = start-end 
    slope = rise / run 

    return round(slope,2)

def calc_slope_data(elev, slope, dist, step):
    dist_list = []
    elev_list = []

    for each_dist in range(dist):
        diff = each_dist * slope 
        new_elev = elev - diff
        
        dist_list.append(each_dist)
        elev_list.append(round(new_elev,2))

        file = open('slope.csv','w') 
        file.write(str(dist_list))
        file.write('\n')
        file.write(str(elev_list)) 

    file.close() 

    style.use('ggplot')
    fig = plt.figure()
    ax = fig.add_subplot(111, facecolor='#f2f2f2')

    for each_cor in range(0, dist, step):
        label_elev = elev - diff 
        box = dict(boxstyle = 'round4', fc = '#19f0f7', ec = '#eeeeee', lw = 1)
        ax.annotate(
            '{} , {} '.format(dist_list[each_cor], elev_list[each_cor]),
                (dist_list[each_cor], elev_list[each_cor]), 
                    xytext = (dist_list[each_cor]  - 0, elev_list[each_cor] + .5) , bbox = box)

    ax.plot(dist_list, elev_list, '#f71993', label = 'Slope: {}' .format(slope))

    cursor = Cursor(ax, useblit=True, color='#666666', linewidth=1)    
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.title('Slope Formula')
    plt.legend()
    plt.show()

'''calc_slope(start, end, run)'''
# s = calc_slope(50, 100,100)
# print(s)

'''calc_slope_data(elev, slope, dist, step)'''
calc_slope_data(44, .5, 60, 5)

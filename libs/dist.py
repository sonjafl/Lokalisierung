'''
Created on 13.10.2013

@author: Sonja Flemming
'''
import numpy as np

def dist(x0,x1,y0,y1):#calculates distance between two points
    erdradius=6371
    lat1 = np.radians(x0)
    lon1 = np.radians(x1)
    lat2 = np.radians(y0)
    lon2 = np.radians(y1)
    dlon = lon1 - lon2

    y=np.sqrt((np.cos(lat2)*np.sin(dlon))**2+(np.cos(lat1)*np.sin(lat2)-np.sin(lat1)*np.cos(lat2)*np.cos(dlon))**2)
    x = np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)*np.cos(dlon)
    c = np.arctan2(y,x)
    return erdradius*c

def dist_tor(x0,x1,tor):#calculates distance between a point and the Brandenburg Gate
    return dist(x0,x1,tor[0],tor[1])


def dist_sat(x0,x1, points_sat):#calculates shortest distance between a point and the satellie's path
    sat_entf=[]
    for i in points_sat:
        sat_entf.append(dist(x0,x1,i[0],i[1]))
    return min(sat_entf)
  
def dist_spree(x0,x1, points_spree):#calculates shortest distance between a point and the river Spree
    spree_entf=[]
    for i in points_spree:
        spree_entf.append(dist(x0,x1,i[0],i[1]))
    return min(spree_entf)       
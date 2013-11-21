'''
Created on 14.10.2013

@author: Sonja Flemming
'''
#from libs.dist import dist


from libs.probabs import w_tor
from libs.probabs import w_sat
from libs.probabs import w_spree
from libs.probabs import w_total
#from libs import points
from libs.points import *

#import matplotlib.pyplot as plt
map_tor_only_w=[]#list of all gridpoints with their tor-probability
map_sat_only_w=[]#list of all gridpoints with their sat-probability
map_spree_only_w=[]#list of all gridpoints with their spree-probability
map_w_only_w=[]#list of all gridpoints with their total probability


def build_maps_only_w():#used for plotting
    for j in range(len(points_map)):
        map_tor_only_w_j=[]
        map_sat_only_w_j=[]
        map_spree_only_w_j=[]
        map_w_only_w_j=[]
        
        for i in range(len(points_map)):
            map_tor_only_w_j.append((w_tor(points_map[j][i][0],points_map[j][i][1])))
            map_sat_only_w_j.append((w_sat(points_map[j][i][0],points_map[j][i][1])))
            map_spree_only_w_j.append((w_spree(points_map[j][i][0],points_map[j][i][1])))
            map_w_only_w_j.append((w_total(points_map[j][i][0],points_map[j][i][1])))
        
        map_tor_only_w.append(map_tor_only_w_j)
        map_sat_only_w.append(map_sat_only_w_j)
        map_spree_only_w.append(map_spree_only_w_j)
        map_w_only_w.append(map_w_only_w_j)
  

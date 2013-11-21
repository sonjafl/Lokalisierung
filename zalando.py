'''
Created on 13.10.2013

@author: Sonja Flemming
'''
from libs.dist import *
from libs.probabs import *
from libs.map import *
from libs.points import *

import matplotlib.pyplot as plt

class zalando(object):
 
    def init(self):
        """ init geo data """
        build_points_sat()
        build_points_spree()
        build_points_map()
        build_maps_only_w()
    
   
    def main(self):
        self.plotmap()
      
    
    def plotmap(self):
        x=longitudes
        y=latitudes
        
        x_axis = np.asarray(x)
        y_axis= np.asarray(y)
       
        frame1 = plt.gca()
        frame1.axes.get_xaxis().set_ticks([])
        frame1.axes.get_yaxis().set_ticks([])
        
        z=map_w_only_w
        z1=map_tor_only_w
        z2=map_sat_only_w
        z3=map_spree_only_w

        cmap=plt.get_cmap('Reds')
        im = plt.imread('map.jpg')
        extent=[0,len(x_axis),0,len(y_axis)]
        implot = plt.imshow(im,extent=extent,aspect='auto')
       
        
        #z1 = plt.imshow(z1, cmap=cmap, alpha=0.4)
        #plt.title("w_tor")
        #z2 = plt.imshow(z2, cmap=cmap, alpha=0.4)
        #plt.title("w_sat")
        #z3 = plt.imshow(z3, cmap=cmap, alpha=0.4)
        #plt.title("w_spree")
        z = plt.imshow(z, cmap=cmap, alpha=0.4)
        plt.title("w_total")
        
        plt.colorbar()
        
        plt.clim()
        frame1.invert_yaxis()
        plt.show()
        
    
z = zalando()
z.init()
z.main()



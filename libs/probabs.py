'''
Created on 13.10.2013

@author: Sonja Flemming
'''
import numpy as np
from libs.dist import *
from libs.points import points_sat, points_spree, tor

def w_tor(x0,x1):#calculates probability for a location w.r.t. its distance to the Brandenburg Gate
    sigma_2=(-1.5*(np.log(3.877)-np.log(4.700)))**(0.5) 
    mu_2=np.log(4.700)-sigma_2**2/2

    return 1.0/(np.sqrt(2*np.pi)*sigma_2*dist_tor(x0,x1,tor))*np.exp(-(np.log(dist_tor(x0,x1,tor))-mu_2)**2/(2*sigma_2**2))

def w_sat(x0,x1):#calculates probability for a location w.r.t. its distance to the satellite's path
    sigma_3=2.400/1.959964
    mu_3=0.0

    return 1/(sigma_3*np.sqrt(2*np.pi))*np.exp(-0.5*(dist_sat(x0,x1,points_sat)-mu_3)**2/(sigma_3)**2)

def w_spree(x0,x1):#calculates probability for a location w.r.t. its distance to the river Spree
    sigma_1=2.730/1.959964
    mu_1=0.0

    return 1/(sigma_1*np.sqrt(2*np.pi))*np.exp(-0.5*(dist_spree(x0,x1,points_spree)-mu_1)**2/(sigma_1)**2)
   
def w_total(x0,x1):#calculates total probability for a point
    return w_tor(x0,x1)*w_sat(x0,x1)*w_spree(x0,x1)

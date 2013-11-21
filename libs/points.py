'''
Created on 13.10.2013

@author: Sonja Flemming
'''
from libs.dist import dist

STEP_SIZE = 0.512
tor=(52.516288,13.377689)
sat=[(52.590117,13.39915),(52.437385,13.553989)]
spree=[(52.529198,13.274099),(52.531835,13.29234),(52.522116,13.298541),(52.520569,13.317349),(52.524877,13.322434),(52.522788,13.329),(52.517056,13.332075),(52.522514,13.340743),(52.517239,13.356665),(52.523063,13.372158),(52.519198,13.379453),(52.522462,13.392328),(52.520921,13.399703),(52.515333,13.406054),(52.514863,13.416354),(52.506034,13.435923),(52.496473,13.461587),(52.487641,13.483216),(52.488739,13.491456),(52.464011,13.503386)]

points_sat = []#all points in satellite path
points_spree = []#all points in river spree
points_map = []#all  points on map
longitudes=[]#all latitudes in map, used for plotting
latitudes=[]#all longitudes in map, used for plotting

# map grid corners
corner_bl=(52.43,13.29)
corner_br=(52.42967019568, 13.56933627316)
corner_tl=(52.60074488805, 13.29)
corner_tr=(52.60041310314, 13.570421)

def build_points_sat():
    d=dist(sat[0][0],sat[0][1],sat[1][0],sat[1][1])
    s=round(d/STEP_SIZE)#number of steps to obtain grid with step-size
    
    for i in range(int(s)+1):
        #adds all points between beginning and end of satellite path
        points_sat.append((sat[0][0]+i/s*(sat[1][0]-sat[0][0]),sat[0][1]+i/s*(sat[1][1]-sat[0][1]))) 
    

def build_points_spree():
    
    for j in range(len(spree)-1):
        
        spree_j=[] #list of pints on j-th section of river spree
        spree_j.append(spree[j])
        spree_j.append(spree[j+1])
        
        d_j=dist(spree[j][0],spree[j][1],spree[j+1][0],spree[j+1][1])
        s_j=round(d_j/STEP_SIZE) #number of steps to obtain gris with size step-size
    
        for i in range(int(s_j)+1):
            #adds all points between j-th and (j+1)st section to spree_j
            spree_j.append((spree_j[0][0]+i/s_j*(spree_j[1][0]-spree_j[0][0]),spree_j[0][1]+i/s_j*(spree_j[1][1]-spree_j[0][1])))
        spree_j.pop()  
        points_spree.extend(spree_j)  #adds j-th section of spree to total spree
        
    points_spree.append(spree[len(spree)-1])

def build_points_map():#devides the map into 1x(step-size)-arrays; this structure is required for plotting
    
    d=dist(corner_bl[0],corner_bl[1],corner_br[0],corner_br[1])

    u=round(d/STEP_SIZE)
    for j in range(int(u)):#up
        points_map_j=[]
        for i in range(int(u)):#right
            #adds all points between j-th and (j+1)st section to spree_j
            points_map_j.append((corner_bl[0]+j/u*(corner_tl[0]-corner_bl[0]),corner_bl[1]+i/u*(corner_br[1]-corner_bl[1]))) 
            if j==0:
                latitudes.append(corner_bl[1]+i/u*(corner_br[1]-corner_bl[1]))
            if i==0:
                longitudes.append(corner_bl[0]+j/u*(corner_tl[0]-corner_bl[0]))
    
        points_map.append(points_map_j) 

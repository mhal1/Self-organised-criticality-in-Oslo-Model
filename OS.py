#oslo model

import numpy as np

import matplotlib.pyplot as plt

class site:

    #initialise site with zero height, zero slope and threshold {1,2}
    
    def __init__(self, p1, p2, height = 0, z_i = 0, topple = False):

        self.__height = 0 # height

        self.__p1 = p1

        self.__p2 = p2

        self.__z_i = z_i

        self.__z_ith = np.random.choice([1,2], p=[p1,p2])

        self.__topple = topple

    def height(self):
        
        return self.__height

    def setheight(self, newheight):

        self.__height = newheight
    
    def z_i(self):

        return self.__z_i

    def set_z_i(self, newz_i):

        self.__z_i = newz_i

    def z_ith(self):

        return self.__z_ith

    def reset_z_ith(self):

        self.__z_ith = np.random.choice([1,2], p=[self.__p1,self.__p2])

    def topple(self):

        return self.__topple

    def set_topple(self, new):

        self.__topple = new

class box:

    def __init__(self, L, N, p1,p2):

        self.__L = L #number of sites

        self.__N = N #number of grains to be added

        self.__p1 = p1

        self.__p2 = p2

        self.__sites = []

        self.__steady = False

        self.__s = 0 # initial avalanche size

        #make list of sites

        for i in range(L):

            self.__sites.append(site(self.__p1,self.__p2))

    def sites(self):

        return self.__sites
            
    def drive(self):

        self.__sites[0].set_z_i(self.__sites[0].z_i() + 1)

        self.__sites[0].setheight(self.__sites[0].height() + 1)

    def steady(self):

        return self.__steady

    def set_steady(self,new):

        self.__steady = new

    ##############################

    def s(self): #avalanche size

        return self.__s

    def set_s(self,new):

        self.__s = new

    ##############################
        
    def relax(self):

        j = 0 #tracking z_j

        self.set_s(0)

        while j <= self.__L-1:

            if self.__sites[j].z_i() > self.__sites[j].z_ith():

                self.__sites[j].set_topple(True)

                ###############################

                if self.steady() == True:

                    self.set_s(self.__s + 1) #add topple to avalanhce size

                ################################

                if j == 0:

                    self.__sites[j].set_z_i(self.__sites[j].z_i() - 2)

                    self.__sites[j+1].set_z_i(self.__sites[j+1].z_i() + 1)

                    self.__sites[j].setheight(self.__sites[j].height() - 1)

                    self.__sites[j+1].setheight(self.__sites[j+1].height() + 1)

                elif j >= 1 and j <= self.__L - 2:

                    self.__sites[j].set_z_i(self.__sites[j].z_i() - 2)

                    self.__sites[j+1].set_z_i(self.__sites[j+1].z_i() + 1)
                    
                    self.__sites[j-1].set_z_i(self.__sites[j-1].z_i() + 1)
                    
                    self.__sites[j].setheight(self.__sites[j].height() - 1)

                    self.__sites[j+1].setheight(self.__sites[j+1].height() + 1)

                elif j == self.__L - 1:

                    self.__sites[j].set_z_i(self.__sites[j].z_i() - 1)

                    self.__sites[j-1].set_z_i(self.__sites[j-1].z_i() + 1)

                    self.__sites[j].setheight(self.__sites[j].height() - 1)

                    self.set_steady(True)
                
                self.__sites[j].reset_z_ith()

            else:

                self.__sites[j].set_topple(False)

            if self.__sites[j].topple() == False:

                j += 1
                
            elif self.__sites[j].topple() == True:

                j -= 1

                if j < 0:

                    j = 0

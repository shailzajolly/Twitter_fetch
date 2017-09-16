# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file which writes a file with names of images in an order

"""

import glob, os
import numpy as np
import re
label = "0"
#os.chdir("/Users/shailzajolly/Downloads/DF/Scripts/test_company/")
os.chdir("/home/jolly/images_verified/")
for filename in sorted(glob.glob("*.jpg"),key=lambda):
    print(filename)
    f = open("/home/jolly/i_v_1.txt","a+") #opens file with name of "test.txt"
    #f.write(filename + "\t" + label + "\n") 
    f.write(filename + "\t" + label +  "\n")  
    f.close()

    #np.savetxt('myfile.txt',(file,label), delimiter=' ', newline= '\n')
    

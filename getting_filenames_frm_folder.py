# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file. The script opens a folder and for each file in the folder it stores the file name in .txt file along with an additional label. This is useful for data preprocessing of CNN
"""

import glob, os
import numpy as np
label = "1"
os.chdir("/Users/shailzajolly/Downloads/DF/Scripts/logos_fortune_500/company_logos")
for filename in glob.glob("*.jpg"):
    #print(file)
    f = open("/Users/shailzajolly/Downloads/DF/Scripts/non_company_users/non_company_logos/test.txt","a+") #opens file with name of "test.txt"
    f.write(filename + "\t" + label + "\n")   
    f.close()

    #np.savetxt('myfile.txt',(file,label), delimiter=' ', newline= '\n')
    

#The screen crawls all the documents in mongoDB and stores screen_names and profile image urls of all verified users in users_name.txt and users_name.csv.

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:02:04 2017

@author: shailzajolly
"""
import pymongo
import numpy as np

from pymongo import MongoClient

client = MongoClient(host="192.168.33.181", port=27020)

db = client.twitterData_1_6

counter = 1
#total documents in a collection
docs_no = db.userData_1_6.count()
print docs_no

usn = []
urls = []
#iterate from all the docs in this collection
a = db.userData_1_6

for doc in a.find():
    
    usn.append(doc['screen_name']) 
    urls.append(doc['profile_image_url'])
    
    #wget.download(image,out= "image" + str(counter) + ".jpg")
    #counter += 1
    print doc['screen_name']
    print doc['profile_image_url']
    
#writing list to csv file
np.savetxt('verfied_users_name.csv',usn,newline='\n',fmt='%s')

np.savetxt('verfied_users_name.txt',urls,newline='\n',fmt='%s')




    
    

#The script reads non_company_users and download their profile images to be used by CNN.

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 23:11:06 2017

@author: shailzajolly
"""

from access_tokens import *
import numpy as np 
import wget
import time

ids=[] 

def from_csv(company_list):
    for company in company_list:
        user = api.get_user(company)
        print company
        print user.friends_count
        ids = get_users_friends(company)
        
        #write_ids_to_csv(ids)
        #print "Saved Successfully"
        
        #non_company_ids = np.genfromtxt('non_companies_ids.csv', delimiter='\n')
        #ids1 = list(non_company_ids)
        
        if len(ids) < 100:
            user_lookup_from_csv(ids)
        else:
           x = 0
           for i in xrange(len(ids)/100 + 1):   #get_users/lookup takes 100 users/request
               y = x + 100
               sub_ids = ids[x:y]
               user_lookup_from_csv(sub_ids)
               
               time.sleep(2)
               x = y

               
def get_users_friends(company):
    ids=[] 
    for page in tweepy.Cursor(api.friends_ids, screen_name=company).pages():
        ids.extend(page)
        print(len(ids))
    
    return ids
    
def write_ids_to_csv(str):
    np.savetxt("non_companies_ids.csv", ids, delimiter='\n')
    

def user_lookup_from_csv(ids1):
     users = api.lookup_users(user_ids= ids1 )
     for u in users:
         media_file = u.profile_image_url
         
         wget.download(media_file,out=u.name+ ".jpg")

def main():
    company_array = np.genfromtxt('non-company-account_users_list.csv',delimiter='\n',dtype=str)
    company_list = list(company_array)
    from_csv(company_list)
        
if __name__ == "__main__":
    main()

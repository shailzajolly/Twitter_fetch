#The script reads .csv file and downloads its profile picture

import wget
import numpy as np
from access_tokens import *

company_array = np.genfromtxt('Fortune_500_companies_new.csv',delimiter='\n',dtype=str)
company_list = list(company_array)
company_list_length = len(company_list)

counter = 0
#users = api.search_users('Berkshire Hathaway')
#print users
#companies_not_found = [] 

for company in company_list:  
    print company
    #split_value = company.split()
    #joined_value = "".join(split_value)    
    #time.sleep(2)
    #user = api.search_users(company)
    user = api.get_user(company)
    #counter1 = 0
    #for user in users:
     #   if (user.name == (joined_value)) or (user.name == (company)):
            #print user.name
            
    media_file = user.profile_image_url
    wget.download(media_file,out=user.name+".jpg")
    #counter=+1
     #       counter1 =+1
    
    #if counter1 == 0:
        #companies_not_found.append(company)
       
#if not companies_not_found is False:
   # np.savetxt("companies_not_found.csv", companies_not_found, delimiter='\n')
        
    
#print "Total logos:" + str(counter)

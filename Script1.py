#The script uses twitter api to fetch ids of all verified users and stores them in output_1_6.csv.

from pymongo import MongoClient
import tweepy
import time
import csv
from access_tokens import *

client = MongoClient(host="192.168.33.181", port=27020)

db = client.twitterData_1_6

#ids=[] #empty list which using {} was dict


#def limit_handled(cursor):
#    while True:
#        try:
#            yield cursor.next()
#        except tweepy.RateLimitError:
#            print(len(ids))
#            print('sleeping Now....')
#            time.sleep(15 * 60)
#            print('restarting Now....')
            
            
def write_2_csv(data):
    with open("output_1_6.csv",'w+') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(data)
        
def append_csv(data):
    with open("output_1_6.csv",'a') as resultFile:
        wr = csv.writer(resultFile)
        wr.writerow(data)

def get_users_followers(str):  
    for page in tweepy.Cursor(api.followers_ids, screen_name=str).pages():
        ids.extend(page)
        time.sleep(60)
        
def get_users_friends(str):
     ids =[]
     for page in tweepy.Cursor(api.friends_ids, screen_name=str).pages():
        ids.extend(page)
        print(len(ids))
        print('sleeping now..')
        time.sleep(60)
        print('restarting now..')
        
     return ids
    
def get_users_lists(ids):
    users = api.lookup_users(user_ids= ids )
    for u in users:
        uj = u._json
        result = db.userData.insert_one(uj)


def main():
    #get_users_followers("jollyshailza")
    
    ids = get_users_friends("verified")
    write_2_csv(ids)
    #print len(ids)
    #get_users_lists(ids)
    

if __name__ == "__main__":
    main()

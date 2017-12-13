#The file inserts data to mongodb, data is about users holding verified status. It reads output_1_6.csv file which contains ids, use lookup function of twitter api and stores data in mongoDB.

from pymongo import MongoClient
import tweepy
import time
import csv
from access_tokens import *

client = MongoClient(host="192.168.33.181", port=27020)

db = client.twitterData_1_6

def read_csv(fileName):
    f = open(fileName)
    rd = csv.reader(f)
    ids = list(rd)
    rows = len(ids)
    id_list = []
    for row in xrange(rows): 
        id_list += ids[row]
    return id_list

def update_lookup(ids):
    x = 0
    for i in xrange(len(ids)/100 + 1):
        y = x + 100
        print(x,y)
        sub_ids = ids[x:y]
        
        get_users_lists(sub_ids)
        time.sleep(3)
        
        x = y

def get_users_lists(ids):
    users = api.lookup_users(user_ids= ids )
    for u in users:
        uj = u._json
        result = db.userData_1_6.insert_one(uj)
        
def main():
    fileName = 'output_1_6.csv'
    ids = read_csv(fileName)
    update_lookup(ids)
    
    
if __name__ == "__main__":
    main()

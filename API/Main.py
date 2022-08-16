import code
from unittest import result
import requests 
import json
from requests.api import get
from requests.api import post


def searchpost():
    resonse_searchpost= requests.post("https://skillbanc.com/ObjectTag/SearchPost?sessionId=d2dd88d2-5989-4322-93a6-61d3916c3812&cname=Hello World App&oname=vikram222.raj.vj@gmail.com&c2name=Hello World&appId=IP App")
    if(resonse_searchpost.status_code==200):
    
        searchpost=resonse_searchpost.json()
        data=searchpost['result']['Objects']
        print("response:")
        print(" ")
        print(" ")
        print(data)
        
    else:
        print(resonse_searchpost.status_code)
    
    

def savepost():
    name= input("enter First name:  ")
    print(" ")
    print(" ")
    response_savepost=requests.post("https://skillbanc.com/ObjectTag/SavePost?sessionId=d2dd88d2-5989-4322-93a6-61d3916c3812&c1name=Hello World&o1name=vikram222.raj.vj@gmail.com : Hello World : 8/8/2022 1:14:55 PM&c2name=First Name&appId=IP App&o2name="+name)
    if(response_savepost.status_code==200):
        savepost=response_savepost.json()
        data2= savepost['o1name']
        print(" ")
        print(" ")
        print(data2)
        print("Changes Made")
       
    else:
        print(response_savepost.status_code)
    return data2

#driver code
searchpost()
print(" ")
savepost()




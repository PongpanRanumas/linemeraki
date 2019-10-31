#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:03:36 2019
@author: nphuntha
"""

from flask import Flask, request, abort
#from meraki import meraki
import requests
import json
import os
import sys

api_key = '52b4d8e2b0184e09b86059607b33655c641f531f'
baseUrl = 'https://api.meraki.com/api/v0'
networkId = 'L_602356450160822827'
meraki_headers = {'x-cisco-meraki-api-key': api_key, 'content-type': 'application/json'}

meraki = Flask(__name__)

def orgdetail():
    org_url = 'https://dashboard.meraki.com/api/v0/organizations'
    OrgRes = requests.get(org_url, headers=meraki_headers)
    OrgOut = json.loads(OrgRes.text)
    text = '\nYou have an organzation id and name :\n\n'
    for row in OrgOut:
       text = text + "Org ID: " + str(row['id']) + "\nOrg Name: " + row['name'] + "\n\n"  
    return(text)
    
#orgdetail()
#networkdetail()
#NetworkName()
#ClientCount()
#Licenselist()

if __name__ == "__main__":
  meraki.run(host='0.0.0.0',port=os.environ['PORT'])

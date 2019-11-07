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

api_key = '3fef26503381c0657934fd9c646f32c8d1c85deb'
baseUrl = 'https://api.meraki.com/api/v0'
networkId = 'L_610800699462131530'
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

def networkdetail():  
    NetworkURL = 'https://api.meraki.com/api/v0/networks/'+ networkId
    NetRes = requests.request("GET", NetworkURL, headers=meraki_headers)
    Network_output = json.loads(NetRes.text)
    text = 'Your network detail :\n\n'
    text = text + "Network id is         :" + Network_output['id']
    text = text + "\nOrganization id is    :" + Network_output['organizationId']
    text = text + "\nOrganization name is  :" + Network_output['name']
    text = text + "\ntimeZone is           :" + Network_output['timeZone']
    return(text)

def NetworkName():  
    NetNameURL = 'https://api.meraki.com/api/v0/organizations/610800699462124274/networks'
    NetName = requests.request("GET", NetNameURL, headers=meraki_headers)
    Network_Name = json.loads(NetName.text)
    networkcount = str(len(Network_Name))
    text = '\nYou have ' + networkcount + ' networks :\n\n'
    print("")
    for Name in Network_Name:
       text = text + str(Name['name']+ "\n")
    return(text)

def ClientCount():  
    ClientURL = 'https://api.meraki.com/api/v0/networks/'+ networkId +'/clients?perPage=100'
    ClientName = requests.request("GET", ClientURL, headers=meraki_headers)
    ClientValue = json.loads(ClientName.text)
    client_count = str(len(ClientValue))
    text = '\nYou have ' + client_count + ' active devices in your network\n'
    for Name in ClientValue:
        text = text + "\nIP "+str(Name['ip']) + " MAC " +str(Name['mac'])
    return(text)

def Licenselist():  
    LicenseURL = 'https://api.meraki.com/api/v0/organizations/610800699462124274/licenseState'
    LicenseName = requests.request("GET", LicenseURL, headers=meraki_headers)
    LicenseValue = json.loads(LicenseName.text)
    #text = Text + str(LicenseValue['licensedDeviceCounts'])
    #print("You have license are \n"+ text)
    text = ("You have license are \n")
    text = text + str(LicenseValue['licensedDeviceCounts'])
    return(text)
    
#orgdetail()
#networkdetail()
#NetworkName()
#ClientCount()
#Licenselist()

if __name__ == "__main__":
  meraki.run(host='0.0.0.0',port=os.environ['PORT'])

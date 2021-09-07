#!/usr/bin/python3

print("Content-type:text/html")
print("Access-Control-Allow-Origin:*")
print()

import cgi
import json
import requests
import xmltodict

data = cgi.FieldStorage()
num = data.getvalue("number")
user="automationtest"
r=requests.get(f"http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={num} &username={user}")
data=xmltodict.parse(r.content)
jdata=json.dumps(data)
df=json.loads(jdata)
df1=json.loads(df['Vehicle']['vehicleJson'])

jsonop=json.dumps(df1)

print(jsonop)

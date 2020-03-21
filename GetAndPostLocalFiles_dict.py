! /usr/bin/env python3
import os
import requests
from collections import defaultdict

# Please replace 
url = 'http://35.222.144.81/feedback/'

# 辞書の初期化
fb_dict = defaultdict(str)

# get feedback(fb) list
filepath = '/data/feedback'
files  = os.listdir(filepath)

# traverse each files
for file in files:
  f = open('/data/feedback/'+file, "r")
  line = f.readlines()
  f.close()

  fb_dict['title'] = line[0][:-1]
  fb_dict['name'] = line[1][:-1]
  fb_dict['date'] = line[2][:-1]
  fb_dict['feedback'] = line[3][:-1]

  response = requests.post(url, json=fb_dict)
  print(response.status_code)

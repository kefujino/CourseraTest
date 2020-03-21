! /usr/bin/env python3
import os
import requests
from collections import defaultdict

# Please replace
url = 'http://<corpweb-external-IP>/feedback'

# 辞書の初期化
fb_dict = defaultdict(list)

# get feedback(fb) list
filepath = '/data/feedback'
files  = os.listdir(filepath)

# traverse each files
for file in files:
  f = open('/data/feedback/'+file, "r")
  line = f.readlines()
  f.close()

  fb_dict['title'].append(line[0][:-1])
  fb_dict['name'].append(line[1][:-1])
  fb_dict['date'].append(line[2][:-1])
  fb_dict['feedback'].append(line[3][:-1])

  #response = requests.post(url, json=fb_dict)
  #print(response.status_code)

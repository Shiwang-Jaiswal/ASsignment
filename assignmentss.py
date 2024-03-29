# -*- coding: utf-8 -*-
"""assignmentSS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GfnSD80PmMRZyUxeruh5fvv69cWFCwlL
"""

import urllib.request

url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
urllib.request.urlretrieve(url, '1.json')

import json
with open("1.json", 'r') as f:
    datastore = json.load(f)

print(datastore)

import pandas as pd
df = pd.DataFrame.from_dict(datastore['products'],orient='index')

df.head()

df['popularity'] = df['popularity'].astype(int)

df.dtypes

df = df.sort_values(by='popularity',ascending=False)
df.head()

df.to_csv('1.csv')
df.to_html('1.html')
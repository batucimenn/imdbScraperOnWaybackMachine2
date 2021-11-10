#!/usr/bin/env python
# coding: utf-8

# Adding links to file and writing to csv.

# In[ ]:


import sys
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep
import json
import csv
import re
import os
import pandas as pd


# File path to save. Ex: C:\Users\User\Desktop\newFolder

# In[ ]:


filePath = input("File path: "+"r'")


# According to which csv should the html be collected? Ex: random100

# In[ ]:


csvName = input("Csv name: ")


# In[ ]:


df = pd.read_csv (csvName+'.csv',encoding='latin-1')
titleList=[]
for i in df:
    titleList.append(df[i])
    str(titleList)
    for i in range(len(df)):
        try:
            index=titleList[0][i]
            film='https://www.imdb.com/title/'+titleList[0][i]
            print(film)
            os.chdir(filePath)
            os.system("mkdir "+index)
            url = 'http://web.archive.org/cdx/search/cdx?url='+film+'/&collapse=digest&from=20070228&to=2022&output=json'
            urls = rq.get(url).text
            parse_url = json.loads(urls)
            url_list = []
            for i in range(1,len(parse_url)):
                try:
                    orig_url = parse_url[i][2]
                    tstamp = parse_url[i][1]
                    waylink = 'https://web.archive.org/web/'+tstamp+'/'+orig_url
                    url_list.append(waylink)
                except:
                    pass
            with open(filePath+'/'+index+"/"+index+"_links"+".csv", mode='w', newline='') as yeni_dosya:
                yeni_yazici = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                yeni_yazici.writerow(['Links'])
                yeni_dosya.close()
            for link in url_list:
                try:
                    with open(filePath+'/'+index+"/"+index+"_links"+".csv", mode='a', newline='') as yeni_dosya:
                        yeni_yazici = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                        yeni_yazici.writerow([link])
                        yeni_dosya.close()
                except:
                    pass
            for i in range(len(url_list)):
                try:
                    final_url=url_list[i]
                    req = rq.get(final_url).text
                    file = open(filePath+"/"+index+"/"+url_list[i][28:40]+".html","w")
                    file.write(req)
                    file.close()
                    sleep(3)
                except:
                    pass
        except:
            pass


# In[ ]:





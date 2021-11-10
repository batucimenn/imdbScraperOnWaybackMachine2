#!/usr/bin/env python
# coding: utf-8

# Enter the number you want to scraper randomly, write it to the file. Write the rest to another file.

# In[ ]:


import pandas as pd
import numpy as np
import csv
import requests as rq
import json


# Filename entry. Ex: films.csv

# In[ ]:


fileName = input("File name: ")


# Random movie count entry.

# In[ ]:


randomMovieCount = input("Random movie count: ")


# How many html files should the movie contain at least?

# In[ ]:


htmlCount = str(input("Html count: "))


# In[ ]:


config1=pd.read_csv(fileName, sep=';', encoding='latin-1')


# In[ ]:


df=config1.drop('Film', axis=1)


# In[ ]:


df2=df.drop('Year', axis=1)


# If the csv file contains 1 column of shifted data: df3=df2.drop('Unnamed: 3',axis=1)

# In[ ]:


df3 = df2


# In[ ]:


with open("random"+randomMovieCount+".csv", mode='w', newline='') as newFile:
    newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    newWriter.writerow(['Title'])
    newFile.close()


# In[ ]:


with open("nonrandom"+randomMovieCount+".csv", mode='w', newline='') as newFile:
    newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    newWriter.writerow(['Title'])
    newFile.close()


# In[ ]:


a=0
limit=0
while a < int(randomMovieCount):
    try:
        a += 1
        randomValue=np.random.randint(1,len(df3))
        randomIndex=df3.iloc[randomValue]
        onlyTitles=randomIndex['Title']
        url = 'http://web.archive.org/cdx/search/cdx?url='+'https://www.imdb.com/title/'+onlyTitles+'/&collapse=digest&from=20070228&to=2022&output=json'
        print(url)
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
        print(len(url_list))
        if len(url_list)>htmlCount:
            limit+=1
             #Choose over 1000 movies that meet your requirements from a random selection of movies
            if limit <1000: 
                with open("random"+randomMovieCount+".csv", mode='a', newline='') as newFile:
                        newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                        newWriter.writerow([onlyTitles])
                        newFile.close()             
                print(randomIndex['Title'])
                print(limit)
    except:
        pass


# In[ ]:


config2=pd.read_csv('random'+randomMovieCount+'.csv', sep=';', encoding='latin-1')


# In[ ]:


for i in df3:
    url_list = df3[i]


# In[ ]:


for i in config2:
    url_list2 = config2[i]


# In[ ]:


url_list3 = np.setdiff1d(url_list,url_list2)
    


# In[ ]:


for i in url_list3:
    print(i)
    with open("nonrandom"+randomMovieCount+".csv", mode='a', newline='') as newFile:
                    newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                    newWriter.writerow([i])
                    newFile.close() 


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# Scraper movies data from Imdb

# In[ ]:


import csv
import pandas as pd


# Year range to collect data.

# In[ ]:


startYear=int(input("startYear: "))
finishYear=int(input("finishYear: "))


# File path to save. Ex: C:\Users\User\Desktop\newFile

# In[ ]:


filePath = input("File path: "+"r'")+("/")


# Create csv and set the titles.

# In[ ]:


with open(filePath+str(startYear)+"_"+str(finishYear)+".csv", mode='w', newline='') as yeni_dosya:
    yeni_yazici = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    yeni_yazici.writerow(['Title'+";"+'Film'+";"+'Year'])
    yeni_dosya.close()


# Download title.basics.tsv.gz from https://datasets.imdbws.com/. Extract data.tsv, print it into csv.

# In[ ]:


with open("data.tsv",encoding="utf8") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")      
    for line in tsvreader:
        try:
            ceviri=int(line[5])
            if(ceviri>=startYear and ceviri<=finishYear and (line[1]=="movie" or line[1]=="tvMovie")):               
                print(line[0]+";"+line[3]+";"+line[5]+";"+line[1])                
                line0=line[0].replace("\"","")
                line5=line[5].replace("\"","")      
                with open(filePath+str(startYear)+"_"+str(finishYear)+".csv", mode='a', newline='') as yeni_dosya:
                    yeni_yazici = csv.writer(yeni_dosya, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                    yeni_yazici.writerow([line0+";"+line[3]+";"+line5])
                    yeni_dosya.close()
        except:
            pass  


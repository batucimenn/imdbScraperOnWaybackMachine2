#!/usr/bin/env python
# coding: utf-8

# Scraper all data(movies, series... ) from Imdb

# In[ ]:


import csv


# Year range to collect data.

# In[ ]:


startYear=int(input("startYear: "))
finishYear=int(input("finishYear: "))


# File path to save.

# In[ ]:


filePath = input("File path: "+"r'")+("/")


# Create csv and set the titles.

# In[ ]:


with open(filePath+str(startYear)+"_"+str(finishYear)+".csv", mode='w', newline='') as newFile:
    newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
    newWriter.writerow(['Title'+";"+'Film'+";"+'Year'])
    newFile.close()


# Download title.basics.tsv.gz from https://datasets.imdbws.com/ . Extract data.tsv
# Print it into csv.

# In[ ]:


with open("data.tsv",encoding="utf8") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
        try:
            integer=int(line[5])
            if(integer>=startYear and integer<=finishYear and line[6]=="\\N"):
                print(line[0]+";"+line[3]+";"+line[5])
                yillar=(line[0]+";"+line[3]+";"+line[5])
                with open(filePath+str(startYear)+"_"+str(finishYear)+".csv", mode='a', newline='') as newFile:
                    newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                    newWriter.writerow([line[0]+";"+line[3]+";"+line[5]])
                    newFile.close()
        except:
            pass
         


#!/usr/bin/env python
# coding: utf-8

# Python code that extracts the date, rating and number of votes from the html pages we save and saves it in a file we specify.

# In[ ]:


import os
from bs4 import BeautifulSoup as bs
import re
import requests as rq
from urllib.request import urlopen
import csv


# The file path of the data we have.

# In[ ]:


dataLocation = input("Data Location: "+"r'")+("/")


# File path to save.

# In[ ]:


saveLocation = input("Save Location: "+"r'")+("/")


# The block of code that assigns all html files to the titles array.

# In[ ]:


titles=[]
entries = os.listdir(dataLocation)
for entry in entries:
    titles.append(entry)


# In[ ]:


a=len(titles)


# Access to all html files is provided with two for loops. (The first allows the progress of the files in the location we selected, the other allows the progress of the content of the files).
# The working logic of the code is to decompose the html structure depending on BeatifulSoup and take the required place. Imdb's website has changed many times over the years. This means that the html structure changes. Therefore, it is necessary to control the change with if blocks that cover the date ranges in the change times. After checking the date, the data we need is taken from the necessary html tags and saved in 'csv' format.

# In[ ]:


url_list = []
for i in range(0,len(titles)):
    finalurl=titles[i]
    with open(saveLocation+finalurl+".csv", mode='w', newline='') as newFile:
        newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
        newWriter.writerow(['Year'+";"+'Month'+";"+'Day'+";"+'Hours'+";"+'Rating'+";"+'Vote'])
        newFile.close()
    filePath=os.listdir(dataLocation+finalurl[0:17])
    for j in range(0,len(filePath)):
            try:
                    url="file:///"+dataLocation+finalurl+"/"+filePath[j]
                    page = urlopen(url);
                    soup = bs(page, "lxml");
                    dateTime=int(url[-17:-9])                     
                    if(dateTime>=20070228 and dateTime<=20070331):
                        try:
                            class2 = soup.find(class_='rating')
                            tag2 = class2.find_all('b')
                            tag3 = class2.find_all('a')
                            print(url[-17:-5]+";"+tag2[1].contents[0].replace('/10','')+";"+tag3[2].contents[0].replace('votes','').replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[1].contents[0].replace('/10','')+";"+tag3[2].contents[0].replace('votes','').replace(',','')])
                                newFile.close()
                        except:
                            pass
                    elif(dateTime>=20070401 and dateTime<=20080531):
                        try:
                            class2 = soup.find(class_='general rating')
                            tag2 = class2.find_all('b')
                            tag3 = class2.find_all('a')
                            print(url[-17:-5]+";"+tag2[1].contents[0].replace('/10','')+";"+tag3[0].contents[0].replace('votes','').replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[1].contents[0].replace('/10','')+";"+tag3[0].contents[0].replace('votes','').replace(',','')])
                                newFile.close()
            
                        except:
                            pass
                    elif(dateTime>=20080601 and dateTime<=20091231):
                        try:
                            class2 = soup.find(class_='meta')
                            tag2 = class2.find_all('b')
                            tag3 = class2.find_all('a')
                            print(url[-17:-5]+";"+tag2[0].contents[0].replace('/10','')+";"+tag3[0].contents[0].replace('votes','').replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[0].contents[0].replace('/10','')+";"+tag3[0].contents[0].replace('votes','').replace(',','')])
                                newFile.close()
                        except:
                            pass
                    elif(dateTime>=20100101 and dateTime<=20100930):
                        try:
                            class2 = soup.find(class_='starbar-meta')
                            tag2 = class2.find_all('b')
                            tag3 = class2.find_all('a')
                            print(url[-17:-5]+";"+tag2[0].contents[0].replace('/10','')+";"+tag3[0].contents[0].replace('votes','').replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[0].contents[0].replace('/10','')+";"+tag3[0].contents[0].replace('votes','').replace(',','')])
                                newFile.close()
                        except:
                            pass
                    elif(dateTime>=20101001 and dateTime<=20110731):
                        try:
                            class2 = soup.find(class_='star-box')
                            tag2 = class2.find_all('a')
                            tag3 = class2.find_all('span')
                            print(url[-17:-5]+";"+tag3[13].contents[0]+";"+tag2[11].contents[0].replace(',','').replace('votes',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag3[13].contents[0]+";"+tag2[11].contents[0].replace(',','').replace('votes','')])
                                newFile.close()
                        except:
                            pass
                    elif(dateTime>=20110801 and dateTime<=20151213):
                        try:
                            class2 = soup.find(class_='star-box-details')
                            tag2 = class2.find_all('span')
                            print(url[-17:-5]+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',','')])
                                newFile.close()
                        except:
                            pass
                    elif(dateTime>=20151214 and dateTime<=20160106):
                        try:
                            class2 = soup.find(class_='imdbRating')
                            tag2 = class2.find_all('span')
                            print(url[-17:-5]+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',','')])
                                newFile.close()
                        except:
                            pass
                    elif(dateTime>=20160107 and dateTime<=20160126):
                        try:
                            class2 = soup.find(class_='star-box-details')
                            tag2 = class2.find_all('span')
                            print(url[-17:-5]+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',','')])
                                newFile.close()
                        except:
                            pass
                    
                    elif(dateTime>=20160127 and dateTime<=20220101):
                        try:
                            class2 = soup.find(class_='imdbRating')
                            tag2 = class2.find_all('span')
                            print(url[-17:-5]+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',',''))
                            with open(saveLocation+finalurl+".csv", mode='a', newline='') as newFile:
                                newWriter = csv.writer(newFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
                                newWriter.writerow([url[-17:-13]+";"+url[-13:-11]+";"+url[-11:-9]+";"+(url[-9:-7]+":"+url[-7:-5])+";"+tag2[0].contents[0]+";"+tag2[3].contents[0].replace(',','')])
                                newFile.close()
                        except:
                             pass
                        
            except:
                pass


# In[ ]:





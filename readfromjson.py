import json
from pprint import pprint
import html2text
from bs4 import BeautifulSoup
#import matplotlib.pyplot as plt
urls=[]

def calcprec(links,manuallinks,prec):
    ct=0
    for i in range(prec):
        t1=links[i].encode('utf-8')
        t2=manuallinks[i].rstrip()
        if(t1==t2):
            ct+=1
    t=ct/float(prec)
    return t

def algo1(urls,glink,ylink,commonlinks):
    algo1res=[0 for i in range(len(urls))]
    temp=[]
    for url in commonlinks:
        in1=glink.index(url)
        in2=ylink.index(url)
        
        pos=min(in1,in2)
        
        algo1res[pos]=url
        """
        temp.append([pos,url])
    temp=sorted(temp,key=lambda l:l[0])
    for i in range(len(commonlinks)):
        algo1res[i]=temp[i][1]"""
    for url in urls:
        if(url not in algo1res):
            if url in glink:
                pos=glink.index(url)
            else:
                pos=ylink.index(url)
            while(algo1res[pos]!=0):
                pos+=1
            algo1res[pos]=url
    
    f=open("ResultantRanks_A1.txt","w")
    for url in algo1res:
        f.write(str(url)+"\n")
    return algo1res

def algo2(urls,glink,ylink,commonlinks):
    algo2res=[0 for i in range(len(urls))]
    temp=[]
    for url in urls:
        if(url in glink):
            in1=glink.index(url)
        else:
            in1=0
        
        if(url in ylink):
            in2=ylink.index(url)
        else:
            in2=0
        pos=in1+in2
        """
        algo1res[pos]=url
        """
        temp.append([pos,url])
    temp=sorted(temp,key=lambda l:l[0])
    for i in range(len(urls)):
        algo2res[i]=temp[i][1]
    


    f=open("ResultantRanks_A2.txt","w")
    for url in algo2res:
        f.write(str(url)+"\n")
    return algo2res  
    
def printagg(commonlinks):
    f=open("aggregateddata.txt","w")
    for i in range(len(gdata)):
        f.write(gtitsnippet[i])
        urls.append(glink[i])
    for i in range(len(ydata)):
        if ylink[i] not in commonlinks:
            f.write(ytitsnippet[i].encode('utf-8'))
            urls.append(ylink[i])
    f.close()
    
def read_raw_json(inputfile,outputfile):
    path='/home/anchit/py/irproject2/googleresults/googleresults/'+inputfile
    with open(path) as data_file:    
        data = json.load(data_file)
    f=open(outputfile+"urls.txt",'w')
    for i in range(len(data)):
        f.write(data[i]["link"]+"\n")
    f.close()
    f=open(outputfile+"titleandsnippet.txt","w")
    for i in range(len(data)):
        string=outputfile+str(i+1)
        data[i]["docid"]=string
        data[i]["link"]=data[i]["link"].encode('utf8')
        data[i]["desc"]=BeautifulSoup(data[i]["desc"]).get_text().strip()
        data[i]["title"]=BeautifulSoup(data[i]["title"].encode('utf8')).get_text().strip()
        f.write(string.encode('utf8')+"    :"+data[i]["title"].encode('utf8')+" "+data[i]["desc"].encode('utf8')+"\n\n\n")      
    f.close()
    return data

gdata=read_raw_json("t2.json","google")
ydata=read_raw_json("items2.json","yahoo")

glink=[]
ylink=[]
gtitsnippet=[]
ytitsnippet=[]
for i in range(len(gdata)):
    glink.append(gdata[i]["link"])
    gtitsnippet.append(gdata[i]["docid"]+"    :"+gdata[i]["title"].encode('utf-8')+" "+gdata[i]["desc"].encode('utf-8')+"\n\n\n")    

for i in range(len(ydata)):
    ylink.append(ydata[i]["link"].encode('utf8'))
    ydata[i]["title"]=ydata[i]["title"].encode('utf8')
    ydata[i]["desc"]=ydata[i]["desc"].encode('utf8')    
    ytitsnippet.append(ydata[i]["docid"]+"    :"+ydata[i]["title"].decode('utf-8')+" "+ydata[i]["desc"].decode('utf-8')+"\n\n\n")

commonlinks= set(glink).intersection(ylink)
printagg(commonlinks)

algo1res=algo1(urls, glink, ylink,commonlinks)
algo2res=algo2(urls, glink, ylink,commonlinks)

gprec=[]
yprec=[]

with open("RankedDocuments.txt") as f:
    manuallinks=f.readlines()
for i in range(6):
    t=calcprec(algo1res,manuallinks,5*(i+1))
    gprec.append(t)
    t=calcprec(algo2res, manuallinks,5*(i+1))
    yprec.append(t)
    
print gprec
print yprec
#plt.plot(gprec,gprec)
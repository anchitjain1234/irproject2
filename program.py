import json
from pprint import pprint
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
urls=[]
import pylab
pylab.ion()

def spearmancoeff(manuallinks,testlink):
    x=[]
    y=[]
    for i in range(len(manuallinks)):
        if(manuallinks[i] in testlink):
            x.append(i+1)
            y.append(testlink.index(manuallinks[i])+1)
    d=[]
    for i,j in zip(x,y):
        k=i-j
        d.append(k*k)
    coeff=1-(6*sum(d))/float((len(y)*(len(y)*len(y)-1)))
    return "{0:.2f}".format(coeff)

def calcprec(links,manuallinks,prec):
    ct=0
    for i in range(prec):
        t1=links[i].encode('utf-8')
        if((t1 in manuallinks) and manuallinks.index(t1)<5):
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
    path='googleresults/googleresults/'+inputfile
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

gdata=read_raw_json("gtest.json","google")
ydata=read_raw_json("ytest.json","yahoo")

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
al1prec=[]
al2prec=[]

print "\n\nPlease manually rank the urls and enter in RankedDocuments.txt . "
n=raw_input("Enter any key to proceed.\n\n")

with open("RankedDocuments.txt") as f:
    manuallinks=f.readlines()
    
for i in range(len(manuallinks)):
    manuallinks[i]=manuallinks[i].rstrip()

for i in range(6):
    t=calcprec(algo1res,manuallinks,5*(i+1))
    al1prec.append(t)
    t=calcprec(algo2res, manuallinks,5*(i+1))
    al2prec.append(t)
#print al1prec
#print al2prec

plt.gca().set_color_cycle(['blue', 'yellow'])
A=[5,10,15,20,25,30]
plt.plot(A,al1prec,label="Best Rank Preicision",linestyle='--', marker='o')
plt.plot(A,al2prec,label="Borda's Approach Precision", marker='o')
plt.axis([0,35,0,1])

# Place a legend to the right of this smaller figure.
plt.legend(bbox_to_anchor=(.05, .97), loc=2, borderaxespad=0.)
for xy in zip(A, al1prec):                                                # <--
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points')
    
for xy in zip(A, al2prec):                                                # <--
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points')


mapalgo1=sum(al1prec)/float(6)
mapalgo2=sum(al2prec)/float(6)

print "\nMAP for Best Rank Approach= "+str(mapalgo1)
print "MAP for Borda's Approach= "+str(mapalgo2)

algo1spearman=spearmancoeff(manuallinks, glink)
print "Spearman coefficient for Best Rank Approach= "+str(algo1spearman)
algo2spearman=spearmancoeff(manuallinks, ylink)
print "Spearman coefficient for Borda's Approach= "+str(algo2spearman)
print "\nPlease check output files generated \n"
n=raw_input("\n\nEnter any key to proceed.")
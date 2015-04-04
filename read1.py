import json
from pprint import pprint

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
        f.write(string.encode('utf8')+"    :"+data[i]["title"].encode('utf8')+" "+data[i]["desc"].encode('utf8')+"\n\n\n")      
    f.close()

read_raw_json("t2.json","google")
read_raw_json("items2.json","yahoo")







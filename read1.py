import json
from pprint import pprint

def read_raw_json(inputfile,outputfile):
    path='/home/anchit/py/irproject2/googleresults/googleresults/'+inputfile
    with open(path) as data_file:    
        data = json.load(data_file)
    f=open(outputfile,'w')
    for i in range(len(data)):
        f.write(data[i]["link"]+"\n") 
    f.close()

read_raw_json("t2.json","googleresultsordered.txt")
read_raw_json("items2.json","yahooresultsordered.txt")







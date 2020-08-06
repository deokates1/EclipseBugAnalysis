
import csv 
import os
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET 
 
data=[]
requiredfields=["bug_id","creation_ts","bug_when","product","component"]
def parseXML(xmlfile):
   
    root= "Error: ParseError: not well-formed (invalid token)"
    try:
        # create element tree object 
        tree = ET.parse(xmlfile) 
      
        # get root element 
        root = tree.getroot() 
        #print(root.tag)
        for child in root:
            tempData=[]
            tempData.append(xmlfile)
            print("=="*10)
            print(child.tag, child.attrib)
            print("***"*10)
            for element in child:
                x=element.tag
                x=x.lower()
                x=x.strip()
                try:
                    b=requiredfields.index(x)
                except ValueError:
                    pass
                else:
                    print(element.tag, ":", element.text)
                    tempData.append(x)
                    tempData.append(element.text)
            data.append(tempData)
                    
        root=root.tag
    except:
        pass
    finally:
        return root

mypath="D:/Project/Project/eclipse-bugs"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)'
with open('xmlHere.csv', 'w+') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(onlyfiles)
tags=[]
i=0
for files in onlyfiles:
    if(i==25):
        pass
    pairs=[]
    reqPath=mypath+ "/" + str(files.strip())
    pairs.append(reqPath)
    all1=parseXML(reqPath)
    pairs.append(all1)
    tags.append(pairs)
    i=i+1

try:
    os.remove("data.csv")
    os.remove("xmlParsed1.csv") 
except:
    pass
 
with open('data.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data)

with open('xmlParsed1.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(tags)

csvFile.close()
print(len(tags))
print("###"*60)
print(tags.count(0))
print("-"*60)


    
    
    
    
    
    
    
    
    
    
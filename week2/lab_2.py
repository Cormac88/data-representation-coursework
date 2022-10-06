import requests as rq
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = rq.get(url)

doc = parseString(page.content)
# Check it works
#print(doc.toprettyxml())  
# Output to console comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later
'''with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)'''

# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r
# adding the newline= '' parameter

retrieveTags = ['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]


with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter ='\t', quotechar='"', 
    quoting = csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        #print (traincode)
        dataList = []
        for retrieveTag in retrieveTags:
            if traincode.startswith("D"):
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
                dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

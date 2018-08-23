import csv
import statistics
import datetime
#AddValues to Dictionary
def addValuesToDictionary(keyID, value):
    
    isWorkStation = matchIP(keyID, "192.168.2.10-250", "Workstation~")
    if(isWorkStation == False):
        isWorkStation = matchIP(keyID, "10.200.150.1-255" , "Internet~")
    dictValueUsingKey = None
    
    #If isWorkstation returns False
    if(isWorkStation == False):
        #dictValueUsingKey returns False if keyID is not in dictionary otherwise returns keyID value
        dictValueUsingKey = getValue(keyID, dictionary)

        #isInstance is True if keyID does not exist in dictionary 
        if(isinstance(dictValueUsingKey , bool)):
            
            ##value += 1
##IF you want the IP of the device that does not exist in the dictionary instead of increment from 0,
##delete the line, "value += 1" and add the line, "value = keyID"
            value = keyID

            #Add the value to the dictionary
            dictionary[keyID] = value
            
            return value, isWorkStation, value
    return value, isWorkStation, dictValueUsingKey   

#AddValues to vertexDictionary
def addValuesToVertexDictionary(keyID, value):
    
    vertexIDExist = getValue(keyID, vertexDictionary)

    #If vertexIDExists == False (does not exist in dictionary), add value to vertexDictionary
    if(isinstance(vertexIDExist, bool)):
        value += 1
        vertexDictionary[keyID] = value

    return value, vertexIDExist

#AddValues to 
def addLocalEdgeDictionary(key, connection):

    vertex1 = connection[0]
    vertex2 = connection[1]
      
    connectionString = str(vertex1) + ":" + str(vertex2)
    
    edgeIDExist = getValue(key, localEdgeDictionary)

    #If edgeIDExists == False (does not exist in dictionary), add value to localEdgeDictionary
    if(isinstance(edgeIDExist, bool)):

        value = []
        value.append(connectionString)
        value.append(1)
        localEdgeDictionary[key] = value
        
    else:
        count = edgeIDExist[1]
        count += 1
        edgeIDExist[1] = count
        localEdgeDictionary[key] = edgeIDExist

def removeIP(connection):
    connection = connection.split(":")
    source = connection[0]
    source = source.split("~")
    source = source[0]
    destination = connection[1]
    destination = destination.split("~")
    destination = destination[0]
    connection = source+destination
    return connection

def createEdge(nodeA, nodeB, vertexID):
    
    if(nodeA != 0):

        addLocalEdgeDictionary(str(nodeA) + " " + str(nodeB), vertexID)
        
    nodeA = nodeB

    return nodeA, nodeB

#Print dictionary 
def printDictionary():
    print(dictionary)
    print(values)

#Returns True if key exists in dictionary else False
def inDictionary(ID):
    return ID in dictionary

#Print keys and values
def dictionaryGetAll():
    print("Id: Values")
    for idKey in dictionary:
        print(str(idKey), dictionary[idKey])

#Print keys and values
def dictionaryGetKey(value):
    for idKey in dictionary:
        if(getValue(idKey, dictionary)== value):
            print(idKey)

#Returns the value using a keyID, if values does not exist --> return False
def getValue(keyID, data):
    return data.get(keyID, False)

def toGraph(vertexID, vertexValue, nodeA, nodeB):

    ##Holds all the verticiesText from the current tuple in the dataset
    vertexText = ""
    ##Holds all the edgeText from the current tuple in the dataset   
    edgeText = ""
    #Loop through the vertexID List
    for i in range (0, len(vertexID)):

        vertexValue, vertexIDExist = addValuesToVertexDictionary(vertexID[i], vertexValue)

        #If a vertexID does not exist in the vertexDictionary [isinstance(vertexIDExist, bool) is True]
        if(isinstance(vertexIDExist, bool)):
            nodeB = vertexValue
            vertexText += ("v " + str(vertexValue) + " " + str(vertex[i]) + "\n")
        else:
            nodeB = vertexIDExist

        #Create labels between verticies
        nodeA, nodeB = createEdge(nodeA, nodeB, vertexID)

    #Rest nodeA
    nodeA = 0
    return vertexValue, vertexText

def matchIP(IP, mask, message):	       
    splitted_IP = IP.split('.')
    for index, current_range in enumerate(mask.split('.')):
        if '-' in current_range:
            mini, maxi = map(int,current_range.split('-'))
        else:
            mini = maxi = int(current_range)
        #If the IP is not in the mask, return False
        try:
            if not (mini <= int(splitted_IP[index]) <= maxi):
                return False
        except:
            print(splitted_IP)
            print(splitted_IP[index])
            input("Above is the error")
    #Returns "Office Workstation" if IP is within the mask
    return message + IP

def copyEdge():

    for idKey in localEdgeDictionary:
        value = localEdgeDictionary[idKey]
        globalEdgeKey = value[0]
        globalEdgeKey = removeIP(globalEdgeKey)
        value = value[1]

        edgeExistInGlobal = getValue(globalEdgeKey, globalEdgeDictionary)
        #If vertexIDExists == False (does not exist in dictionary), add value to globalEdgeDictionary
        if(isinstance(edgeExistInGlobal, bool)):
            globalEdgeValue = []
            globalEdgeValue.append(value)
            globalEdgeDictionary[globalEdgeKey] = globalEdgeValue
        else:
            edgeExistInGlobal.append(value)
            globalEdgeDictionary[globalEdgeKey] = edgeExistInGlobal
        
def writeGFile():
    
    for x in vertexTextCollection:   
        newFile.write(x)
        
    for idKey in localEdgeDictionary:
        
        comment = localEdgeDictionary[idKey]
        comment = comment[0] + "#" + str(comment [1])
        newFile.write("d " + idKey + " //" + str(comment) + "\n")
        
#Replace the values in the Global Edge Dictionary with SD and Mean 
def calculateStatisticsGlobalEdge():

    dataList = None
    #First element is mean and the second element is the mean
    statisticsResults = None

    countFile = open('results9Count.txt', 'w+')
    
    for idKey in globalEdgeDictionary:
        dataList = globalEdgeDictionary[idKey]

        countFile.write(idKey)
        countFile.write("\n" + str(dataList) + "\n")

        #If there is more than one element in the dataList
        if(len(dataList)>=2):
            #calculate the SD
            sd = statistics.stdev(dataList)
            #Find 2x deviation 
            sd = sd*2
            #calculate the mean
            mean = statistics.mean(dataList)

            statisticsResults = mean + sd
        else:
            #0 is appended to the list if there is only one number
            statisticsResults = 0

        #Change the dictionary value to the statistics Results
        globalEdgeDictionary[idKey] = statisticsResults

        #Reset the statistics list
        statisticsResults = None
    countFile.write("\nGlobal Edge Dictionary:\n")
    countFile.write(str(globalEdgeDictionary))
    countFile.close()
        
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#The "value" variable in the dictionary
dictionaryValueIncrement = -1
#Create Dictionary that gives all vaues in the dataset unique IDS
dictionary = {"10.200.150.1": "Firewall to Internet","172.20.1.1": "Firewall to EWS","172.20.1.5": "External Web",
              "192.168.1.16": "Snort IDS to Network","192.168.1.1": "Firewall to Data Center VLAN","192.168.2.1": "Firewall to Office VLAN",
              "192.168.1.2": "DHCP","192.168.1.3": "HR DB","192.168.1.4": "Shipping/Routing DB",
              "192.168.1.5": "Internal Web","192.168.1.6": "Mail Server","192.168.1.7": "File Server",
              "192.168.1.14": "DNS","192.168.1.50": "Firewall Log"}
#Holds the vertex in a XP
vertexDictionary = {}

#Holds the edges in a XP
localEdgeDictionary = {}

#Holds the edges in whole doc 
globalEdgeDictionary = {}

#Open newfile if new file does not exist create file (option '+'). optioon 'a' is for appending
newFile = open('results9.g', 'w+')
#Holds the port text
port = ""
#Holds each tuple from the csv file (source IP, source port, destionation port, destionation IP)
vertex = [0]*2
#This increments from 0 and is the first numeric value in the vertex output 
vertexValue = 0
#Holds the edge label between the two ports
edgeLabel = ""
#Holds node A when creating an edge
nodeA = 0
#Holds node B when creating an edge
nodeB = 0
#Holds all the vertex Text
vertexTextCollection = []

#True if the return value is a workStation
isWorkStation = ""
#Value variable in the dictionary (returned)
dictionaryValue = ""
#Holds the firewall tuple time
timeA = None
timeB = None
xpTimeStamp = None
#The XP number
XP = 2
secondsIntervals = None

##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#The meaning of each index in row for the csvReader
##0 dateTime
##1 sysLogPriority 
##2 operation 
##3 messageCode 
##4 protocol 
##5 sourceIP 
##6 destIP 
##7 sourceHostName 
##8 destHostName 
##9 sourcePort 
##10 destPort 
##11 destService 
##12 direction 
##13 connectionBuilt 
##14 connectionTornDown

print("Start Program")
newFile.write("//Time seperated by " + str(secondsIntervals) + " sec\n")
newFile.write("XP # 1 //")
with open('test.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    
    #Skip the header
    next(csvReader, None)
    timeB = next(csvReader, None)[0]

    #Print the time comment
    newFile.write(timeB + "\n")

    #Rest CSV file
    csvfile.seek(0)
    #Skip the header
    next(csvReader, None)
    
    #Add Everything to the Dictionary 
    for row in csvReader:
        #If the source IP is "(empty)" skip the evaulation of the row
        if(row[5] == "(empty)"):
            continue
        
        ##0 dateTime
        timeB = row[0]
        
        ##1 sysLogPriority 
        ##2 operation
        edgeLabel = row[2]
        ##3 messageCode 
        ##4 protocol 
        ##5 sourceIP
        dictionaryValueIncrement, isWorkStation, dictionaryValue = addValuesToDictionary(row[5], dictionaryValueIncrement)
        #The IP is not a Work Station and the IP is not in the predefined devices
        if(isWorkStation == False):
            #The vertx will be a vertex created by the dicitonaryValueIncrement
            vertex[0] = dictionaryValue
        else:
            vertex[0] = isWorkStation
        
        ##6 destIP
        dictionaryValueIncrement, isWorkStation, dictionaryValue = addValuesToDictionary(row[6], dictionaryValueIncrement)
        #The IP is not a Work Station and the IP is not in the predefined devices
        if(isWorkStation == False):
            #The vertx will be a vertex created by the dicitonaryValueIncrement
            vertex[1] = dictionaryValue
        else:
            vertex[1] = isWorkStation
        ##7 sourceHostName
        ##8 destHostName 
        ##9 sourcePort        
        ##10 destPort        
        ##11 destService 
        ##12 direction 
        ##13 connectionBuilt 
        ##14 connectionTornDown
            
        #Breaks it down into minute intervals instead of fraction of seconds
        xpTimeStamp = timeB
        timeB = datetime.datetime.strptime(timeB, '%d/%b/%Y %H:%M:%S')
    
        if(timeA == None):
            timeA = timeB 

        #If the times don't match (skipping the evaluation of the time in the first tuple)
        if(timeA < timeB):        
            
            writeGFile()
            
            #Reset Vertex Dictionary because vertex compression needs to be reset
            vertexValue = 0
            vertexDictionary = {}
            #copy edge from local edge dictionary to global edge dictioanry
            copyEdge()
            localEdgeDictionary = {}
            #Creates the vertex for the graphs
            vertexValue,  vertexText = toGraph(vertex, vertexValue, nodeA, nodeB)
            #Notice: Current collecitons only has vertex and time from the previous tuple
            
            newFile.write("XP # " + str(XP) + " //" + xpTimeStamp + "\n")
            XP += 1
                
            #Reset the collection
            vertexTextCollection = []

            #Update time
            timeA = timeB 
        else:
            #Creates the vertex for the graphs
            vertexValue, vertexText = toGraph(vertex, vertexValue, nodeA, nodeB)

        #Add the returned text to their collection
        if(vertexText != ""):
            vertexTextCollection.append(vertexText)

        
    #copy edge from local edge dictionary to global edge dictioanry
    copyEdge()

    writeGFile()

newFile.close()
print("Part Two")

calculateStatisticsGlobalEdge()
print("\n")
    
file = open('results9.g','r')
newFile = open('results9Final.g', 'w+')
for line in file:
    
    word = line.split()
    if(word[0] == "d"):
        edge = None
        #Split the comment into: comment, connection, globalEdgeKey, and count
        comment = line.split("//")
        connection = comment[0]
        comment = comment[1]
        comment = comment.split("#")
        #Grab the count
        count = comment[1]
        count = count.replace("\n", "")
        count = float(count)
        #Grab the comment
        comment = comment[0]

        #Remove IP to get Key
        globalEdgeKey = removeIP(comment)

        #Holds the 2SD + Mean
        globalEdgeDictionaryValue = globalEdgeDictionary[globalEdgeKey]
        
        #Create Edge Label
        #globalEdgeDictionaryValue is 1 if the deviation is 1
        #globalEdgeDictionaryValue is 0 if the deviation cannot be calculated
        if(globalEdgeDictionaryValue > 1):
            if(count > globalEdgeDictionaryValue):
                edge = "high"
            else:
                edge = "mid"
        else:
            edge = "mid"
        newFile.write(connection + "\""+ edge + "\" //" + comment + " #" + str(count) +"\n")
    elif(word[0] == "v"):

        vertexPartA = word[0] + " " + word[1]
        vertexPartB = word
        del vertexPartB[0:2]
        vertexPartB = " ".join(vertexPartB)
        vertexComment = vertexPartB.split("~")
        
        if(len(vertexComment) > 1):
            newFile.write(vertexPartA + " \"" + vertexComment[0] + "\" //" + vertexComment[1] + "\n")
        else:
            newFile.write(vertexPartA + " \"" + vertexPartB + "\"\n")
            
    else:
        newFile.write(line)

file.close()
newFile.close()

print("End Program")
input("Press Any Key to Exit ")

    



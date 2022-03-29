# Open file
inputFile='/home/nuclear-pig/Stuff/DataAnalytics/Classes/Python/simple-python-data-structures/input_data/democracy-in-decline.txt'

try:
    fh=open(inputFile,"r")
except:
    print("ERROR. Unable to open file.")
    quit()

# Read file into variable
fileVariable=fh.read()

# Convert file to upper case for fair comparison
fileVarUpper=fileVariable.upper()
#print(fileVarUpper)

# Split file into list, based on blank space
fileList=fileVarUpper.split()
#print(fileList)
print(len(fileList))

# Remove websites included in the text
fileListNoWeb=list()
discardedWebList=list()
websiteMarkerList=('/','.','@','-')
for item in fileList:
    webSymbTrack=0
    for marker in websiteMarkerList:
        if marker in item:
            webSymbTrack=webSymbTrack+1;
    if webSymbTrack < 2:
        fileListNoWeb.append(item)
    if webSymbTrack > 2:
        discardedWebList.append(item)
#print(fileListNoWeb)
print(len(fileListNoWeb))

# Remove punctuation from the text
fileListNoWebPunc=list()
punctuationList=(',','/','\\','?','!','-','@','.','\"')
for item in fileListNoWeb:
    #print(item)
    for punc in punctuationList:
        #print(punc)
        if punc in item:
            itemSplit=item.split(punc)
            item=itemSplit[0]
            #print(item)
    fileListNoWebPunc.append(item)
print(fileListNoWebPunc)
print(len(fileListNoWebPunc))
print(discardedWebList)

# Count words
fileHist=dict()
for item in fileListNoWebPunc:
    fileHist[item]=fileHist.get(item,0)+1
print(fileHist)

# Find the most frequent word
freqCount=0
for word,freq in fileHist.items():
    if freq>freqCount:
        freqWord=word
        freqCount=freq
print(freqCount, freqWord)

# Sort histogram dictionary into a list
print(type(fileHist))
invertFileList=list()
for k,v in fileHist.items():
    invertFileList.append((v,k))
sortedInvertedFileList=sorted(invertFileList)
print("\n\n\n\n",sortedInvertedFileList)

for i in sortedInvertedFileList:
    print(i)

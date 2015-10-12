import re #regular expressions module


URL = 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?'

def createIndex():

    inf = open("CID_SEARCH.txt","r")
    lines = inf.read()

    records = re.findall(r'((INDX=\d+).*?(Spring \d+|Fall \d+))',lines)
    inf.close()

    semester = open("index.txt","w")

    for index in range(len(records)):
        semester.write(records[index][1] + ' ' + records[index][2] + '\n')

    semester.close()

    # print records[0][1], records[0][2]
    # print records[-1][1], records[-1][2]

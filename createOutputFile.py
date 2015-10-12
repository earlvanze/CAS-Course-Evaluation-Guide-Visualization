import requests #http://requests.readthedocs.org/en/latest/
import html2text

# from createIndex import createIndex

URL = 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?'

def main():

#    createIndex()  # Already Done Once

    lines = tuple(open("index4.txt", "r"))
    out = open("out4.txt","w")

    count = 0

    for line in lines:
        line = line.split()
        link = URL + line[0]
#        print link
        r = requests.get(link, auth=('evc228', 'Whoorah4'))
#        print line[0], line[1], line[2]
        result = html2text.html2text(r.text)
        data = link + '\nSemester: ' + line[1] + ' ' + line[2] + '\n\n' + result
        print data
#        out.write(data)
        count += 1
#        print count
        
    out.close()

if __name__ == main():
    main()

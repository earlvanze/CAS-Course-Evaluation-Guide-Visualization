#import re

def removeURL(lines, index):
    if ( 'CSUBJ&SEARCH_CSUBJ' in lines[index].split('(')[1].split('=') ):
        if ( 'CINSTR&SEARCH_CINSTR' in lines[index+1].split('(')[1].split('=') ):
            lines[index+1] = lines[index+1].split('(')[0] + '\n'
        else:
            lines[index+1] = (lines[index+1].rstrip() + lines[index+2]).split('(')[0]
        if ( 'students' not in lines[index+2].split() ):
            lines.pop(index+2)
        if ('students' not in lines[index+1].split()):
            lines.pop(index+1)
    if ( '(./GEG_REQUEST.php?TYPE=CID&SEARCH_CID' in lines[index].split('=').split('('):
         lines[index].rstrip(']')
    

def removeNBSP(lines, index):
    if lines[index].split()[0] == '&nbsp_place_holder;':
        lines.pop(index)
        

def cleanOutput():
    infile = 'output_test.txt'
    outfile = 'output_new.txt'
    ofs = open(outfile,'w')

    with open(infile,'r') as ifs:
#        lines = ifs.readlines()
#        lines = [l for l in lines if l != '\n']'

        lines = ifs.readlines()
        index = 0
        for line in lines:
            try:
                lines[index]
            except IndexError:
                break
            else:
                try:
                    removeURL(lines, index)
                    print str(index) + ': ' + lines[index]
                    index += 1
                except IndexError:
                    removeNBSP(lines, index)
                    print str(index) + ': ' + lines[index]
                    index += 1
            
#        pattern = re.compile(r"\[([A-Za-z0-9_]+)\]")
#        items[5:6] = [reduce(lambda x, y: x + y, items[5:6])]          
        
#        for index in range(0, len(lines)-1,63):
#            if len((lines[index+6].split())) is not 1:
#                print ( str(index+6) + ': ' + str(lines[index+6]) )
#                lines.insert(index+7, lines[index+6])
#            if index > len(lines):
#                break
#            if lines[index] == '&nbsp_place_holder;\n':
#                lines.pop(index)

        for index in range(0, len(lines)-1):
            ofs.write(lines[index])
            
    ofs.close()

def main():
    cleanOutput()


if __name__ == main():
    main()

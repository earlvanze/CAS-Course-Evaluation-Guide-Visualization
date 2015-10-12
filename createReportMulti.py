from Report import Report
from itertools import islice
from multiprocessing import Process, Lock
import pickle

#ReportInstances = []

'''
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)
'''


def createReport(ifs, ofs):
    while True:
        lines = list(islice(ifs, 62))

        
        'This was for taking care of lines[6] overflow - already done'
#        if ( isinstance( lines[6].split()[0], (int) ) is False ):
#        if len((lines[6].split())) is not 1:
#            lines.insert(7, lines[6])
#            inf_lines.insert(7, inf_lines[6])
#            print inf_lines[6].split()[0]

        if not lines:
            break
        
        # process next_n_lines

        for index in range(0, len(lines)-1):
            print ( str(index) + ': ' + str(lines[index]) )
        
        inst = []
        cr = []
        rec = []

        'Course Evaluation'
        ev=[]
        ev.append(lines[0].split()[0])
        ev.append(lines[1][-len(lines):-1].split()[1])
        ev.append(lines[1][-len(lines):-1].split()[2])
        ev.append(lines[2].split()[0])
        ev.append(lines[3].split(']')[0].split('[')[1])
        ev.append(lines[4].split(']')[0].split('[')[1])
#        print str(5) + ': ' + str(lines[5].split())
        ev.append(lines[5])
        print str(6) + ': ' + str(lines[6].split())
        ev.append(lines[6].split()[0])
        ev.append(lines[6].split()[2])
        ev.append(lines[6].split()[3].split('(')[1])
        ev.append(inst)
        ev.append(cr)
        ev.append(rec)
        '''for index in range(0, len(ev)-1):
            print str(index) + ': ' + str(ev[index])
            print'''

        'Instructor Rating'
        inst.append(lines[10].split()[0])
        inst.append(lines[12].split()[0])
        inst.append(lines[14].split()[0])
        inst.append(lines[16].split()[0])
        inst.append(lines[20].split()[0])
        inst.append(lines[58].split()[0].split(' || '))
#            for index in range(0, len(inst)-1):
#                print inst[index]
#                print

        'Course Rating'
        cr.append(lines[24].split()[0])
        cr.append(lines[26].split()[0])
        cr.append(lines[28].split()[0])
        cr.append(lines[30].split()[0])
        cr.append(lines[32].split()[0])
        cr.append(lines[35].split()[0])
        cr.append(lines[37].split()[0])
        cr.append(lines[39].split()[0])
        cr.append(lines[42].split()[0])
        cr.append(lines[44].split()[0])
        cr.append(lines[60].split()[0].split(' || '))
#            for index in range(0, len(cr)-1):
#                print cr[index]
#                print

        'Discussion/Recitation/Lab Section'
        rec.append(lines[48].split()[0])
        rec.append(lines[51].split()[0])
        rec.append(lines[54].split()[0])
#            for index in range(0, len(rec)-1):
#                print rec[index]
#                print

        'Append report object to list of reports'
        'NOT A GOOD IDEA - HIGHLY MEMORY INTENSIVE'
#            ReportInstances.append(Report(ev))

        'Dump Report Object instances into file - "pickling"'
#            print pickle.dumps( Report(ev) )
        pickle.dump( Report(ev), ofs )

        for index in range(0, len(lines)-1):
            lines.pop()


def main():
    infile = 'output.txt'
    picklefile = 'reportInstances.txt'

    with open(infile,'r') as ifs, open(picklefile,'w') as instances: 
        createReport(ifs, instances)
#        p1 = Process(target=createReport, args=(ifs, instances))
#        p1.start()
    
if __name__ == main():
    main()

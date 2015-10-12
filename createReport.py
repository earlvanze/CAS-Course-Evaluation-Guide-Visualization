from Report import Report
from itertools import islice
import pickle
import pygal

ReportInstances = []

def createReport():

    instances = open('reportInstances.txt','w')
    
    with open("output.txt","r") as inf:
        inf_lines = inf.readlines()
        inf_lines = [l for l in inf_lines if l != '\n']
        
        while True:
            lines = list(islice(inf_lines, 70))
            if ( isinstance( lines[6].split()[0], ( int, long ) ) is False ):
                lines.pop(6)
            if not lines:
                break
            
            # process next_n_lines

            for index in range(0, len(lines)-1):
                print str(index) + ': ' + str(lines[index])
            
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
            ev.append(lines[5].split(']')[0].split('[')[1])
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
            inst.append(lines[12].split()[0])
            inst.append(lines[14].split()[0])
            inst.append(lines[16].split()[0])
            inst.append(lines[18].split()[0])
            inst.append(lines[23].split()[0])
            inst.append(lines[65][-len(lines[65]):-1].split(' || '))
#            for index in range(0, len(inst)-1):
#                print inst[index]
#                print

            'Course Rating'
            cr.append(lines[28].split()[0])
            cr.append(lines[30].split()[0])
            cr.append(lines[32].split()[0])
            cr.append(lines[34].split()[0])
            cr.append(lines[36].split()[0])
            cr.append(lines[40].split()[0])
            cr.append(lines[42].split()[0])
            cr.append(lines[44].split()[0])
            cr.append(lines[47].split()[0])
            cr.append(lines[49].split()[0])
            cr.append(lines[67][-len(lines[67]):-1].split(' || '))
#            for index in range(0, len(cr)-1):
#                print cr[index]
#                print

            'Discussion/Recitation/Lab Section'
            rec.append(lines[54].split()[0])
            rec.append(lines[57].split()[0])
            rec.append(lines[60].split()[0])
#            for index in range(0, len(rec)-1):
#                print rec[index]
#                print

            'Append report object to list of reports'
            ReportInstances.append(Report(ev))

            'Dump Report Object instances into file - "pickling"'
#            print pickle.dumps( Report(ev) )
            pickle.dump( Report(ev), instances )

    instances.close()

def main():
    createReport()

if __name__ == main():
    main()

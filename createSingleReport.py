from Report import Report
import pygal

ReportInstances = []

def createReport():
    inf=open("output.txt","r")
    lines = inf.readlines()
    lines = [l for l in lines if l != '\n']

    inst = []
    cr = []
    rec = []

    'Course Evaluation'
    ev=[]
    ev.append(lines[0][-len(lines[0]):-1])
    ev.append(lines[1][-len(lines):-1].split()[1])
    ev.append(lines[1][-len(lines):-1].split()[2])
    ev.append(lines[2].split()[0])
    ev.append(lines[3].split(']')[0].split('[')[1])
    ev.append(lines[4].split(']')[0].split('[')[1])
    ev.append(lines[5].split(']')[0].split('[')[1])
    ev.append(lines[7].split()[0])
    ev.append(lines[7].split()[2])
    ev.append(lines[7].split()[3].split('(')[1])
    ev.append(inst)
    ev.append(cr)
    ev.append(rec)
    for index in range(0, len(ev)-1):
        print str(index) + ': '
        print ev[index]
        print

    'Instructor Rating'
    inst.append(lines[13].split()[0])
    inst.append(lines[15].split()[0])
    inst.append(lines[17].split()[0])
    inst.append(lines[19].split()[0])
    inst.append(lines[24].split()[0])
    inst.append(lines[66][-len(lines[66]):-1].split(' || '))
    print inst[3]
    for index in range(0, len(inst)-1):
        print inst[index]
        print

    print "FAIRNESS: " + inst[2]

    'Course Rating'
    cr.append(lines[29].split()[0])
    cr.append(lines[31].split()[0])
    cr.append(lines[33].split()[0])
    cr.append(lines[35].split()[0])
    cr.append(lines[37].split()[0])
    cr.append(lines[41].split()[0])
    cr.append(lines[43].split()[0])
    cr.append(lines[45].split()[0])
    cr.append(lines[48].split()[0])
    cr.append(lines[50].split()[0])
    cr.append(lines[68][-len(lines[68]):-1].split(' || '))
    for index in range(0, len(cr)-1):
        print cr[index]
        print

    'Discussion/Recitation/Lab Section'
    rec.append(lines[55].split()[0])
    rec.append(lines[58].split()[0])
    rec.append(lines[61].split()[0])
    for index in range(0, len(rec)-1):
        print rec[index]
        print
    
    ReportInstances.append(Report(ev))

def main():
    createReport()
    print 'URL: ' + str(ReportInstances[0])
    
    pie_chart = pygal.Pie()
    pie_chart.title = 'Would you recommend this instructor to a friend?'
    pie_chart.add('Yes', float(ReportInstances[0].instructorRating.recommendation[0]))
    pie_chart.add('No', float(ReportInstances[0].instructorRating.recommendation[1]))
    pie_chart.render_to_file('pie_chart.svg')

    bar_chart = pygal.Bar()
    bar_chart.title = 'Course Ratings for ' + ReportInstances[0].cid
    bar_chart.add('Overall', float(ReportInstances[0].courseRating.overall))
    bar_chart.add('Clarity of Objectives', float(ReportInstances[0].courseRating.objectivesClarity))
    bar_chart.add('Achievement of Objectives', float(ReportInstances[0].courseRating.objectivesAchievement))
    bar_chart.add('Interesting Course', float(ReportInstances[0].courseRating.interesting))
    bar_chart.add('Expectations Met', float(ReportInstances[0].courseRating.expectationsMet))
    bar_chart.add('Workload', float(ReportInstances[0].courseRating.workload))
    bar_chart.add('Amount of Studying', float(ReportInstances[0].courseRating.amtOfStudy))
    bar_chart.add('Prior Subject Interest', float(ReportInstances[0].courseRating.priorSubjectInterest))
    bar_chart.add('Increased Knowledge of Subject', float(ReportInstances[0].courseRating.increasedSubjectKnowledge))
    bar_chart.add('Recommend Course to a Friend', float(ReportInstances[0].courseRating.recommendation[0])/float(ReportInstances[0].courseRating.recommendation[1]))
    bar_chart.render_to_file('bar_chart.svg')   

if __name__ == main():
    main()

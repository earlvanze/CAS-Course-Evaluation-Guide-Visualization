
In [1]: inf=open("/Users/vphuvan/Downloads/output.txt","r")

In [2]: lines = inf.readlines()


In [3]: lines[0]
Out[3]: 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447\n'

In [4]: lines[1]
Out[4]: 'Semester: Spring 2013\n'

In [5]: lines[2]
Out[5]: 'A History of Disbelief\n'

In [6]: lines[3]
Out[6]: '\n'


In [7]: lines.index('\n')
Out[7]: 3

In [8]: lines = [l for l in lines if l != '\n']



In [9]: lines[0:70]
Out[9]: 
['http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447\n',
 'Semester: Spring 2013\n',
 'A History of Disbelief\n',
 '[AHSEM-UA113001](./GEG_REQUEST.php?TYPE=CID&SEARCH_CID=AHSEM-UA113001)\n',
 '[Advanced Honors Seminars](./GEG_REQUEST.php?TYPE=CSUBJ&SEARCH_CSUBJ=AHSEM-UA)\n',
 '[Mitchell Stephens](./GEG_REQUEST.php?TYPE=CINSTR&SEARCH_CINSTR=Mitchell\n',
 'Stephens)\n',
 '5 of 5 (100 %) students responded\n',
 '&nbsp_place_holder;\n',
 '&nbsp_place_holder;\n',
 'Instructor\n',
 'Average Result (5=Excellent, 1=Poor)\n',
 'How would you rate the instructor overall?\n',
 '4.20\n',
 'How informative were the classes?\n',
 '4.20\n',
 'How well organized were the classes?\n',
 '3.60\n',
 'How fair was the grading?\n',
 '4.60\n',
 '&nbsp_place_holder;\n',
 'Average Result (5=Very, 1=Not at all)\n',
 'To what extent was the primary instructor effective in helping you learn in\n',
 'this course?\n',
 '4.40\n',
 '&nbsp_place_holder;\n',
 'Course\n',
 'Average Result (5=Excellent, 1=Poor)\n',
 'How would you rate this course overall?\n',
 '4.20\n',
 'How clear were the objectives of this course?\n',
 '4.25\n',
 'How well were these objectives achieved?\n',
 '4.00\n',
 'How interesting was the course?\n',
 '4.80\n',
 'To what extent were your own expectations met?\n',
 '4.00\n',
 '&nbsp_place_holder;\n',
 'Average Result (5=Very, 1=Not at all)\n',
 'How heavy was the workload?\n',
 '3.20\n',
 'How much did you study for this course?\n',
 '3.20\n',
 'To what extent were you challenged intellectually by this course?\n',
 '4.80\n',
 'To what extent were you interested in the subject area before taking this\n',
 'course?\n',
 '5.00\n',
 'To what extent was your knowledge in this subject area increased?\n',
 '4.00\n',
 '&nbsp_place_holder;\n',
 'Discussion/Recitation/Lab Section\n',
 'Average Result (5=Very, 1=Not at all)\n',
 'How helpful was the teaching assistant?\n',
 '0.00\n',
 'How good was the communication between the instructor and the teaching\n',
 'assistant?\n',
 '0.00\n',
 'How useful was the discussion/recitation/lab in achieving the objective of\n',
 'this course?\n',
 '0.00\n',
 '&nbsp_place_holder;\n',
 'Recommendation\n',
 'Yes || No\n',
 'Would you recommend this instructor to a friend?\n',
 '4 || 1\n',
 'Would you recommend this course to a friend?\n',
 '4 || 1\n',
 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27448\n']


In [10]: lines[0],lines[69]
Out[10]: 
('http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447\n',
 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27448\n')

In [11]: ReportInstances = []


In [12]: lines[0]
Out[12]: 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447\n'

In [28]: lines[0][-len(lines[0]):-1]
Out[28]: 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447'

In [21]: lines[0] = ines[0][-len(lines[0]):-1]


In [13]: ev=[]

In [14]: ev.append(lines[0])

In [15]: lines[1][-len(lines):-1]
Out[15]: 'Semester: Spring 2013'

In [16]: lines[1][-len(lines):-1].split()
Out[16]: ['Semester:', 'Spring', '2013']

In [17]: lines[1][-len(lines):-1].split()[1]
Out[17]: 'Spring'

In [18]: ev.append(lines[1][-len(lines):-1].split()[1])

In [19]: lines[1][-len(lines):-1].split()[2]
Out[19]: '2013'

In [20]: ev.append(lines[1][-len(lines):-1].split()[2])

In [21]: class Report:
    def __init__(self,ev=[]):
        self.url=ev[0]
   ....:         

In [22]: ev
Out[22]: ['http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447\n','Spring','2013']

In [23]: Report(ev)
Out[23]: <__main__.Report instance at 0x11aea2128>


In [24]: type(ReportInstances)
Out[24]: list

In [25]: ReportInstances.append(Report(ev))

In [26]: ReportInstances[0]
Out[26]: <__main__.Report instance at 0x119ee9d88>

In [27]: ReportInstances[0].url
Out[27]: 'http://www.nyu.edu/cas/ceg/GEG_REQUEST_INDX.php?INDX=27447\n'

In [32]: lines[3]
Out[32]: '[AHSEM-UA113001](./GEG_REQUEST.php?TYPE=CID&SEARCH_CID=AHSEM-UA113001)\n'

In [33]: lines[3].split(']')
Out[33]: ['[AHSEM-UA113001', '(./GEG_REQUEST.php?TYPE=CID&SEARCH_CID=AHSEM-UA113001)\n']

In [34]: lines[3].split(']')[0]
Out[34]: '[AHSEM-UA113001'

In [35]: lines[3].split(']')[0].split('[')
Out[35]: ['', 'AHSEM-UA113001']

In [36]: lines[3].split(']')[0].split('[')[1]
Out[36]: 'AHSEM-UA113001'

In [37]: ev.append(lines[3].split(']')[0].split('[')[1])

In [38]: ev.append(lines[4].split(']')[0].split('[')[1])

In [39]: ev.append(lines[5].split(']')[0].split('[')[1])

In [39]: lines[7]
Out[39]: '5 of 5 (100 %) students responded\n'

In [40]: lines[7].split()
Out[40]: ['5', 'of', '5', '(100', '%)', 'students', 'responded']


In [42]: lines[7].split()[0]
Out[42]: '5'

In [43]: lines[7].split()[2]
Out[43]: '5'

In [44]: lines[7].split()[3]
Out[44]: '(100'

In [45]: lines[7].split()[3].split('(')
Out[45]: ['', '100']

In [46]: lines[7].split()[3].split('(')[1]
Out[46]: '100'


In [47]: ev.append(lines[7].split()[0])

In [48]: ev.append(lines[7].split()[2])

In [49: ev.append(lines[7].split()[3].split('(')[1])


In [53]: lines[9:25]
Out[53]: 
['&nbsp_place_holder;\n',
 'Instructor\n',
 'Average Result (5=Excellent, 1=Poor)\n',
 'How would you rate the instructor overall?\n',
 '4.20\n',
 'How informative were the classes?\n',
 '4.20\n',
 'How well organized were the classes?\n',
 '3.60\n',
 'How fair was the grading?\n',
 '4.60\n',
 '&nbsp_place_holder;\n',
 'Average Result (5=Very, 1=Not at all)\n',
 'To what extent was the primary instructor effective in helping you learn in\n',
 'this course?\n',
 '4.40\n']

In [62]: inst= []

In [63]: lines[13][-len(lines[13]):-1]
Out[63]: '4.20'

In [63]: inst.append(lines[13][-len(lines[13]):-1])

In [63]: lines[15][-len(lines[15]):-1]
Out[63]: '4.20'

In [64]: inst.append(lines[15][-len(lines[15]):-1])

In [65]: lines[17][-len(lines[17]):-1]
Out[65]: '3.60'

In [66]: inst.append(lines[17][-len(lines[17]):-1])

In [67]: lines[19][-len(lines[19]):-1]
Out[67]: '4.60'

In [68]: inst.append(lines[19][-len(lines[19]):-1])

In [70]: lines[24][-len(lines[24]):-1]
Out[70]: '4.40'

In [71]: inst.append(lines[24][-len(lines[24]):-1])


In [78]: lines[65]
Out[78]: 'Would you recommend this instructor to a friend?\n'

In [79]: lines[66]
Out[79]: '4 || 1\n'

In [80]: lines[66][-len(lines[66]):-1]
Out[80]: '4 || 1'

In [81]: lines[66][-len(lines[66]):-1].split(' || ')
Out[81]: ['4', '1']

In [81]: inst.append(lines[66][-len(lines[66]):-1].split(' || '))

In [82]: lines[66][-len(lines[66]):-1].split(' || ')[0]
Out[82]: '4'

In [83]: lines[66][-len(lines[66]):-1].split(' || ')[1]
Out[83]: '1'

cr = []

In [89]: lines[29][-len(lines[29]):-1]
Out[89]: '4.20'

In [89]: cr.append(lines[29][-len(lines[29]):-1])

In [90]: lines[31][-len(lines[29]):-1]
Out[90]: '4.25'

In [91]: cr.append(lines[31][-len(lines[31]):-1])

In [93]: lines[33][-len(lines[33]):-1]
Out[93]: '4.00'

In [94]: cr.append(lines[33][-len(lines[33]):-1])

In [98]: lines[35][-len(lines[35]):-1]
Out[98]: '4.80'

In [99]: cr.append(lines[35][-len(lines[35]):-1])

In [105]: lines[37][-len(lines[37]):-1]
Out[105]: '4.00'

In [106]: cr.append(lines[37][-len(lines[37]):-1])

In [107]: lines[41].split()[0]
Out[107]: '3.20'

In [108]: cr.append(lines[41].split()[0])

In [109]: lines[43].split()[0]
Out[109]: '3.20'

In [109]: cr.append(lines[43].split()[0])

In [110]: lines[45].split()[0]
Out[110]: '4.80'

In [111]: cr.append(lines[45].split()[0])

In [112]: lines[48].split()[0]
Out[112]: '5.00'

In [113]: cr.append(lines[48].split()[0])

In [114]: lines[50].split()[0]
Out[114]: '4.00'

In [115]: cr.append(lines[50].split()[0])

In [150]: lines[68][-len(lines[68]):-1].split(' || ')
Out[150]: ['4', '1']

In [151]: cr.append(lines[68][-len(lines[68]):-1].split(' || '))

In [152]: lines[55].split()[0]
Out[152]: '0.00'

In [153]: rec =  []

In [154]: rec.append(lines[55].split()[0])

In [155]: lines[58].split()[0]
Out[155]: '0.00'

In [155]: rec.append(lines[58].split()[0])

In [156]: lines[61].split()[0]
Out[156]: '0.00'

In [157]: rec.append(lines[61].split()[0])



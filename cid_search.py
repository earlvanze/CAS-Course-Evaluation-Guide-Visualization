

In [1]: inf = open("full_list_html.txt","r")

In [2]: lines = inf.read()

In [3]: record=re.findall(r'((INDX=\d+).*?(Spring \d+|Fall \d+))',lines)

In [4]: record[0]
Out[4]: 
('INDX=27447\\\',\\\'#FFFFFF\\\')" onmouseover="rowOver(1)" onmouseout="rowOut(1,\\\'#CFA8FC\\\')" id="name1">\\n<td>AHSEM-UA113001</td><td>Advanced Honors Seminars</td><td>Mitchell Stephens</td><td>A History of Disbelief</td><td>Spring 2013',
 'INDX=27447',
 'Spring 2013')

In [5]: record[0][0]
Out[4]: 'INDX=27447\\\',\\\'#FFFFFF\\\')" onmouseover="rowOver(1)" onmouseout="rowOut(1,\\\'#CFA8FC\\\')" id="name1">\\n<td>AHSEM-UA113001</td><td>Advanced Honors Seminars</td><td>Mitchell Stephens</td><td>A History of Disbelief</td><td>Spring 2013'

In [6]: record[0][1]
Out[6]: 'INDX=27447'

In [7]: record[0][2]
Out[7]: 'Spring 2013'

In [8]: record[-1]
Out[8]: 
('INDX=9984\\\',\\\'#FFFFFF\\\')" onmouseover="rowOver(26730)" onmouseout="rowOut(26730,\\\'#CFA8FC\\\')" id="name26730">\\n<td>V89.0009001</td><td>Psychology</td><td>Harrington</td><td>Statistical Reasoning For The Behavioral Sci</td><td>Fall 2000',
 'INDX=9984',
 'Fall 2000')

In [9]: record[-1][0]
Out[9]: 'INDX=9984\\\',\\\'#FFFFFF\\\')" onmouseover="rowOver(26730)" onmouseout="rowOut(26730,\\\'#CFA8FC\\\')" id="name26730">\\n<td>V89.0009001</td><td>Psychology</td><td>Harrington</td><td>Statistical Reasoning For The Behavioral Sci</td><td>Fall 2000'

In [10]: record[-1][1]
Out[10]: 'INDX=9984'

In [11]: record[-1][2]
Out[11]: 'Fall 2000'



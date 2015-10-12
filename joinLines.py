from itertools import islice

def joinLines():
    infile = 'output_old4.txt'
    outfile = 'output_new.txt'
    ofs = open(outfile,'w')

    with open(infile,'r') as ifs:
        while True:
            lines = list(islice(ifs, 62))

            if not lines:
                break

            if ( "students" not in lines[6].split() ):
                lines[5] = lines[5].rstrip('\n')+lines[6]
                lines.pop(6)

            for index in range(0, len(lines)-1):
                print lines[index]
                ofs.write(lines[index])

    ofs.close()


def splitSemester():
    infile = 'output.txt'
    outfile = 'output_new.txt'
    ofs = open(outfile,'w')

    with open(infile,'r') as ifs:
        while True:
            lines = list(islice(ifs, 62))

            if not lines:
                break

            if ( "mester" in lines[0].split('Se') ):
                lines[0] = lines[0].split('Se')[0] + '\n'
                string = 'Se' + lines[0].split('Se')[1] + '\n'
                lines.insert(1,string)

            for index in range(0, len(lines)-1):
                print lines[index]
                ofs.write(lines[index])

    ofs.close()

def main():
    splitSemester()

if __name__ == main():
    main()

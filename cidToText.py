def main():

    inf = open('course_id_html.txt','r')
    out = open('course_id.txt','w')

    lines = inf.readlines()

    for line in lines:
        line = line.split('"')[1] + '\n'
        out.write(line)

if __name__ == main():
    main()

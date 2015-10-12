import re

def main():
    inf = open("output_test.txt","r")
    lines = inf.readlines()
    print lines
#    records = re.findall(r'((\]\d+).*?\))',lines)
    records = re.findall(r"\[([A-Za-z0-9_]+)\]",lines)

    for index in range(len(records)):
        print records[index]
        ofs.write(records[index][0])
        
    inf.close()

    ofs = open("output_new.txt",'w')

    ofs.close()

if __name__ == main:
    main()

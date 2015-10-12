import pickle
from multiprocessing import Process

reportInstances = []

def unpickle(inf):

    data = pickle.load(inf)
    reportInstances.append(data)

def main():
    inf = open('instances1.txt','rb')
    p = Process(target = unpickle, args=(inf))
    p.start()
    inf.close()

    for item in reportInstances:
        print item

if __name__ == main:
    main()

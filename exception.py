__author__ = 'Alfred'

try:
    filename = raw_input('Enter filename: ')
    fobj = open(filename, 'r')
    for line in fobj:
        print line
    fobj.close()
except IOError, e:
    print 'file open error: ', e
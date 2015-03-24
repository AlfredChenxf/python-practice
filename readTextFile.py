__author__ = 'Alfred'

# read and display text file

readfile = raw_input('Enter filename for read:')
lines = []

try:
    fobj = open(readfile, 'r')
except IOError, e:
    print 'Can not open this file', e
else:
    for line in fobj:
        print line
    fobj.close()


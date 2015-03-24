__author__ = 'Alfred'
# 3.1

import os
ls = os.linesep

while True:
    userFile = raw_input('Enter filename:')
    if os.path.exists(userFile):
        print 'ERROR: %s is already exists.' %userFile
    else:
        break

lines = []
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        lines.append(entry)

fobj = open(userFile, 'w')
for x in lines:
    fobj.writelines(['%s%s'%(x,ls)])

fobj.close()
print 'Done.'